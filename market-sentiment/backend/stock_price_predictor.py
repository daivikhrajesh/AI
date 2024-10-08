import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM
import yfinance as yf

def prepare_stock_data(ticker):
    data = yf.Ticker(ticker).history(period='5y')
    closing_price = data['Close'].values.reshape(-1, 1)

    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(closing_price)

    return scaled_data, scaler

def create_lstm_model(input_shape):
    model = Sequential()
    model.add(LSTM(50, return_sequences=True, input_shape=(input_shape[1], input_shape[2])))
    model.add(LSTM(50, return_sequences=False))
    model.add(Dense(25))
    model.add(Dense(1))

    model.compile(optimizer='adam', loss='mean_squared_error')
    return model

def train_lstm_model(data, model):
    x_train, y_train = [], []

    for i in range(60, len(data)):
        x_train.append(data[i-60:i, 0])
        y_train.append(data[i, 0])

    x_train, y_train = np.array(x_train), np.array(y_train)
    x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))

    model.fit(x_train, y_train, batch_size=1, epochs=1)

if __name__ == "__main__":
    ticker = 'AAPL'
    data, scaler = prepare_stock_data(ticker)
    lstm_model = create_lstm_model((data.shape[0], 60, 1))
    train_lstm_model(data, lstm_model)
