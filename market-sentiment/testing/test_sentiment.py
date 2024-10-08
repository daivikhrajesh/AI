import unittest
from backend.sentiment_analysis import analyze_sentiment

class TestSentimentAnalysis(unittest.TestCase):

    def test_analyze_sentiment_positive(self):
        text = "The stock market is doing great!"
        result = analyze_sentiment(text)
        self.assertIn('compound', result)
        self.assertGreater(result['compound'], 0, "Expected positive sentiment")

    def test_analyze_sentiment_negative(self):
        text = "The stock market is crashing!"
        result = analyze_sentiment(text)
        self.assertIn('compound', result)
        self.assertLess(result['compound'], 0, "Expected negative sentiment")

if __name__ == '__main__':
    unittest.main()
