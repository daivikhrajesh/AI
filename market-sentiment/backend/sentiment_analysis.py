# import nltk
# from nltk.sentiment.vader import SentimentIntensityAnalyzer

# nltk.download('vader_lexicon')

# def analyze_sentiment(text):
#     sid = SentimentIntensityAnalyzer()
#     scores = sid.polarity_scores(text)
#     return scores

# if __name__ == "__main__":
#     text = "The stock market is doing great!"
#     sentiment = analyze_sentiment(text)
#     print(sentiment)


import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download VADER lexicon if not already done
nltk.download('vader_lexicon')

def analyze_sentiment(text):
    sia = SentimentIntensityAnalyzer()
    return sia.polarity_scores(text)
