import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
import joblib

# Load the sentiment data
df_sentiment = pd.read_csv('sentiment_data.csv')

# Rename the columns to meaningful names
df_sentiment.columns = ['News', 'URL', 'sentiment_score']
print("Sentiment Data Columns:", df_sentiment.columns)

# Load the historical stock data
df_stock = pd.read_csv('historical_stock_data.csv')
print("Stock Data Columns:", df_stock.columns)

# Ensure the 'Date' column in the stock data is in datetime format
df_stock['Date'] = pd.to_datetime(df_stock['Date'])

# Create a new column for sentiment date
# This assumes the sentiment data has a date column; modify as necessary
# For demonstration, let's assume the sentiment data corresponds to dates in sequence
df_sentiment['Date'] = pd.date_range(start='2020-01-01', periods=len(df_sentiment), freq='D')

# Merge the dataframes on the date column
df_merged = pd.merge(df_stock, df_sentiment, on='Date', how='left')

# Print the merged DataFrame's columns
print("Merged Data Columns:", df_merged.columns)

# Dropping rows with NaN values (if any)
df_merged.dropna(inplace=True)

# Now use the renamed column for sentiment score
X = df_merged[['sentiment_score']]  # Use the new name here
y = df_merged['Close']

# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Initialize the model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Print evaluation metrics
print(f'Mean Squared Error: {mse}')
print(f'R-squared: {r2}')

# Save the model using joblib
joblib.dump(model, 'stock_price_predictor.pkl')
