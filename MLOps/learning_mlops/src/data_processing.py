import pandas as pd
import os

def load_data(data_path):
    df = pd.read_csv(data_path)
    return df

def preprocess_data(df):
    # Add any preprocessing steps here
    # For simplicity, we're assuming data is already clean
    return df

if __name__ == "__main__":
    data_path = 'F:\Learning\AI\MLOps\learning_mlops\data\my_dataset.csv'
    df = load_data(data_path)
    processed_data = preprocess_data(df)
    processed_data.to_csv('F:\Learning\AI\MLOps\learning_mlops\data\processed\processed_data.csv', index=False)
