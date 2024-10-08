import unittest
from backend.stock_price_predictor import prepare_stock_data, create_lstm_model, train_lstm_model
import numpy as np

class TestStockPredictor(unittest.TestCase):

    def test_prepare_stock_data(self):
        ticker = 'AAPL'
        data, scaler = prepare_stock_data(ticker)
        self.assertIsInstance(data, np.ndarray, "Stock data should be a numpy array")
        self.assertEqual(data.shape[1], 1, "Expected single feature (Close price)")

    def test_lstm_model_training(self):
        ticker = 'AAPL'
        data, _ = prepare_stock_data(ticker)
        model = create_lstm_model((data.shape[0], 60, 1))
        try:
            train_lstm_model(data, model)
        except Exception as e:
            self.fail(f"LSTM model training failed: {e}")

if __name__ == '__main__':
    unittest.main()
