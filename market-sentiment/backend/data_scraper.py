import requests
from bs4 import BeautifulSoup
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

# Download the VADER lexicon
nltk.download('vader_lexicon')

def scrape_yahoo_finance_news():
    url = 'https://finance.yahoo.com'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    news = []

    # Find news articles (this selector may change depending on the Yahoo Finance page structure)
    for item in soup.find_all('h3'):
        link = item.find('a')
        if link:
            headline = link.text
            news.append((headline, link['href']))

    sentiment_analyzer = SentimentIntensityAnalyzer()
    sentiment_data = []

    for headline, link in news:
        sentiment = sentiment_analyzer.polarity_scores(headline)
        sentiment_data.append((headline, link, sentiment['compound']))

    # Convert to DataFrame and save to CSV
    df = pd.DataFrame(sentiment_data, columns=['headline', 'link', 'compound'])
    df.to_csv('sentiment_data.csv', mode='a', header=False, index=False)

    return sentiment_data

if __name__ == "__main__":
    scrape_yahoo_finance_news()
