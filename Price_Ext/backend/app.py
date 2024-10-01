from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def get_amazon_price(item):
    # Perform a search query on Amazon
    search_url = f"https://www.amazon.com/s?k={item.replace(' ', '+')}"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract the price (this may vary based on the page structure)
    try:
        price = soup.find('span', {'class': 'a-price-whole'}).text
        return f"${price}"
    except AttributeError:
        return "Price not found"

def get_bestbuy_price(item):
    # Perform a search query on Best Buy
    search_url = f"https://www.bestbuy.com/site/searchpage.jsp?st={item.replace(' ', '+')}"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract the price (this may vary based on the page structure)
    try:
        price = soup.find('div', {'class': 'priceView-customer-price'}).span.text
        return price
    except AttributeError:
        return "Price not found"

@app.route('/compare', methods=['POST'])
def compare():
    data = request.json
    item = data['item']
    
    amazon_price = get_amazon_price(item)
    bestbuy_price = get_bestbuy_price(item)

    return jsonify({
        'amazon_price': amazon_price,
        'bestbuy_price': bestbuy_price,
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
