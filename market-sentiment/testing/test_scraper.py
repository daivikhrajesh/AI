import unittest
from backend.data_scraper import scrape_yahoo_finance_news

class TestScraper(unittest.TestCase):

    def test_scrape_yahoo_finance_news(self):
        news = scrape_yahoo_finance_news()
        self.assertIsInstance(news, list)
        self.assertGreater(len(news), 0, "No news articles were scraped")
        self.assertIsInstance(news[0], tuple)
        self.assertEqual(len(news[0]), 2, "News tuple should contain headline and link")

if __name__ == '__main__':
    unittest.main()
