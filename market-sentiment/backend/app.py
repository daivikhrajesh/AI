from flask import Flask, render_template
from newsapi import NewsApiClient
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

# Ensure VADER's lexicon is downloaded
nltk.download('vader_lexicon')

app = Flask(__name__)

# Initialize NewsAPI client (replace 'your_api_key' with your actual NewsAPI key)
newsapi = NewsApiClient(api_key='bfd9c2775b5c4b40be51441b13a3d5ea')

# Initialize VADER sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Fetch latest news headlines related to the stock market
def get_stock_news():
    headlines = []
    articles = newsapi.get_everything(q='stocks', language='en', sort_by='relevancy', page_size=10)
    
    if articles['status'] == 'ok':
        headlines = [article['title'] for article in articles['articles']]
    
    return headlines

# Perform sentiment analysis using VADER
def perform_sentiment_analysis(news_headlines):
    sentiments = []
    
    for headline in news_headlines:
        score = sia.polarity_scores(headline)['compound']
        if score >= 0.05:
            sentiments.append('Positive')
        elif score <= -0.05:
            sentiments.append('Negative')
        else:
            sentiments.append('Neutral')
    
    return sentiments

@app.route('/')
def index():
    # Fetch real stock news headlines
    news_headlines = get_stock_news()
    
    # Perform sentiment analysis
    sentiments = perform_sentiment_analysis(news_headlines)

    return render_template('dashboard.html', news=news_headlines, sentiments=sentiments)

if __name__ == '__main__':
    app.run(debug=True)
