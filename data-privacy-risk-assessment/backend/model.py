import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Load GDPR violations dataset
def load_gdpr_data(filepath):
    try:
        df = pd.read_csv(filepath)
        print(f"Loaded {len(df)} records from {filepath}.")
        return df
    except Exception as e:
        print(f"Error loading GDPR data: {e}")
        return None

# Load Website Phishing dataset
def load_phishing_data(filepath):
    try:
        df = pd.read_csv(filepath)
        print(f"Loaded {len(df)} records from {filepath}.")
        return df
    except Exception as e:
        print(f"Error loading phishing data: {e}")
        return None

# Train a Random Forest model
def train_model(df):
    X = df.drop(columns=['Result'])
    y = df['Result']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    # Evaluate the model
    y_pred = model.predict(X_test)
    print(classification_report(y_test, y_pred))

    return model
