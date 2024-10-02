# backend/price_comparison.py
from bs4 import BeautifulSoup
import requests

def get_amazon_price(item_name):
    amazon_url = f"https://www.amazon.com/s?k={item_name.replace(' ', '+')}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
    }
    response = requests.get(amazon_url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # Find the price element (modify based on current HTML structure)
        price_element = soup.find('span', {'class': 'a-price-whole'})  # Update class if needed
        if price_element:
            return f"${price_element.text}"
        else:
            return "Price not found"
    else:
        return "Price not found"

def get_bestbuy_price(item_name):
    bestbuy_url = f"https://www.bestbuy.com/site/searchpage.jsp?st={item_name.replace(' ', '+')}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
    }
    response = requests.get(bestbuy_url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # Find the price element (modify based on current HTML structure)
        price_element = soup.find('div', {'class': 'price'}).find('span')  # Update class if needed
        if price_element:
            return price_element.text
        else:
            return "Price not found"
    else:
        return "Price not found"
