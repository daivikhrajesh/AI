from flask import Flask, request, jsonify
from model import load_gdpr_data, load_phishing_data
from privacy_risk_assessment import assess_privacy_risk

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Data Privacy Risk Assessment API. Use /assess to assess privacy risk."

@app.route('/assess', methods=['POST'])
def assess():
    data = request.json
    result = assess_privacy_risk(data)
    return jsonify(result)

@app.route('/favicon.ico')
def favicon():
    return '', 204  # No content

if __name__ == '__main__':
    app.run(debug=True)
