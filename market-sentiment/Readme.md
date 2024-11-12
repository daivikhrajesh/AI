# Market Sentiment Analysis and Prediction

## Overview
This project implements a comprehensive market sentiment analysis tool that scrapes financial news and social media content, performs sentiment analysis, fetches historical stock prices, and predicts stock movements using machine learning models. The tool also includes a dashboard for visualization and monitoring sentiment trends and alerts.

## Features
- **Data Scraping**: Scrapes financial news articles and social media posts to gather sentiment data.
- **Sentiment Analysis**: Analyzes the sentiment of the scraped content using various methods.
- **Stock Price Prediction**: Utilizes an LSTM model to forecast future stock prices based on historical data.
- **Sentiment Alerts**: Notifies users when significant sentiment changes occur.
- **Dashboard**: Provides an interactive web interface for monitoring sentiment and stock trends.

## Project Structure
```
market-sentiment/
├── backend/
│   ├── app.py                     # Flask app to serve the dashboard
│   ├── stock_price_predictor.py    # LSTM model to predict stock prices
│   ├── data_scraper.py             # For scraping financial news and social media content
│   ├── stock_price_fetcher.py      # For fetching historical stock prices using yfinance
│   ├── sentiment_analysis.py        # Perform sentiment analysis on the scraped data
│   ├── model_utils.py              # Helper functions for data processing and model training
│   ├── dashboard.py                 # New dashboard implementation
│   ├── sentiment_alerts.py          # New file for sentiment alerts
│   ├── machine_learning.py           # New file for machine learning integration
│   ├── templates/                   # HTML templates for the dashboard
│   │   └── dashboard.html           # HTML file for the dashboard
│   └── requirements.txt             # Updated dependencies for the project
│
├── frontend/
│   ├── static/
│   │   ├── style.css                # CSS for the dashboard styling
│   │   └── script.js                # JavaScript for frontend functionality
│   └── README.md                    # Instructions and project details
│
├── testing/
│   ├── test_scraper.py              # Unit tests for the web scraper
│   ├── test_sentiment.py            # Unit tests for sentiment analysis
│   ├── test_stock_predictor.py      # Unit tests for stock prediction
│
└── README.md                        # Instructions and project details
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/daivikrajesh/market-sentiment.git
   cd market-sentiment
   ```

2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```bash
   pip install -r backend/requirements.txt
   ```

## Usage

### Running the Flask Application
To start the Flask application and serve the dashboard, run:
```bash
python backend/app.py
```
Access the dashboard in your web browser at `http://127.0.0.1:5000`.

### Scraping News and Sentiment Data
To scrape financial news and social media content, run:
```bash
python backend/data_scraper.py
```
This will populate your sentiment analysis data for further processing.

### Performing Sentiment Analysis
To analyze the sentiment of the scraped data, run:
```bash
python backend/sentiment_analysis.py
```

### Fetching Historical Stock Prices
To fetch historical stock prices for your analysis, run:
```bash
python backend/stock_price_fetcher.py
```

### Predicting Stock Prices
To predict stock prices using the LSTM model, run:
```bash
python backend/stock_price_predictor.py
```

### Setting Up Sentiment Alerts
To enable sentiment alerts based on the analysis, run:
```bash
python backend/sentiment_alerts.py
```

### Testing
To run the unit tests for various components of the project, navigate to the `testing` directory and run:
```bash
python -m unittest discover
```

## Technologies Used
- **Python**: Programming language for implementation.
- **Flask**: Web framework for the backend.
- **Pandas**: Data manipulation and analysis.
- **NumPy**: Support for large, multi-dimensional arrays and matrices.
- **Scikit-Learn**: Machine learning library for Python.
- **TensorFlow/Keras**: Framework for building and training the LSTM model.
- **BeautifulSoup**: Library for web scraping.
- **yfinance**: Library for fetching financial data.

## Contributing
Contributions are welcome! Please feel free to submit a pull request or report issues.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
- [Yahoo Finance](https://finance.yahoo.com/) for providing the financial news data.
- [VADER Sentiment Analysis](https://github.com/cjhutto/vaderSentiment) for sentiment analysis tools.
- [scikit-learn](https://scikit-learn.org/stable/) for machine learning algorithms.

```
