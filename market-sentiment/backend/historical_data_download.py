import yfinance as yf

# Define the stock symbol and time frame
stock_symbol = 'AAPL'  # Example: Apple Inc.
start_date = '2020-01-01'
end_date = '2023-12-31'

# Fetch historical data
data = yf.download(stock_symbol, start=start_date, end=end_date)

# Save to CSV
data.to_csv('historical_stock_data.csv')
print("Historical stock data downloaded successfully.")
