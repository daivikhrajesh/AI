import sys
import os
import nltk
from flask import Flask, render_template
import plotly.graph_objs as go
import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer

# Add the parent directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Now import the backend modules
from backend.data_scraper import scrape_yahoo_finance_news
from backend.sentiment_analysis import analyze_sentiment

app = Flask(__name__)
nltk.download('vader_lexicon')

# List to store sentiment data
sentiment_data = []

@app.route('/')
def dashboard():
    # Scrape news articles
    news_articles = scrape_yahoo_finance_news()
    if not news_articles:
        return "No news articles available."

    # Analyze sentiment
    sia = SentimentIntensityAnalyzer()
    sentiments = []
    for headline, _ in news_articles:
        score = sia.polarity_scores(headline)['compound']
        sentiments.append((headline, score))

    # Create a DataFrame for visualization
    df = pd.DataFrame(sentiments, columns=['headline', 'compound'])
    
    # Render the dashboard with the sentiment data
    return render_template('dashboard.html', articles=df.to_dict(orient='records'))

if __name__ == "__main__":
    app.run(debug=True)