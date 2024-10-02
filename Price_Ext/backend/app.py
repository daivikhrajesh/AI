# backend/app.py
from flask import Flask, request, jsonify
from price_comparison import get_amazon_price, get_bestbuy_price  # Import the scraping functions

app = Flask(__name__)

@app.route('/compare', methods=['POST'])
def compare_prices():
    data = request.get_json()
    item_name = data.get('item')

    amazon_price = get_amazon_price(item_name)
    bestbuy_price = get_bestbuy_price(item_name)

    return jsonify({
        "amazon_price": amazon_price,
        "bestbuy_price": bestbuy_price
    })

if __name__ == '__main__':
    app.run(debug=True)
