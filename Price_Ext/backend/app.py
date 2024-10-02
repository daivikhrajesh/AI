from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

def get_amazon_price(item_name):
    # Implement the logic to scrape or fetch the price from Amazon
    # This is just a placeholder implementation
    return 19.99  # Placeholder value

def get_bestbuy_price(item_name):
    # Implement the logic to scrape or fetch the price from Best Buy
    # This is just a placeholder implementation
    return 24.99  # Placeholder value

@app.route('/compare-prices', methods=['POST'])
def compare_prices():
    data = request.get_json()

    if not data or 'item' not in data:
        return jsonify({"error": "Invalid input"}), 400

    item_name = data['item']

    try:
        amazon_price = get_amazon_price(item_name)
        bestbuy_price = get_bestbuy_price(item_name)

        return jsonify({
            "amazon_price": amazon_price,
            "bestbuy_price": bestbuy_price
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
