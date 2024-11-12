import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import mlflow
import mlflow.sklearn

def train_model(data_path):
    # Load data
    df = pd.read_csv(data_path)
    X = df[['feature1', 'feature2']]
    y = df['target']

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    model = RandomForestClassifier(n_estimators=100)
    model.fit(X_train, y_train)

    # Log model
    mlflow.start_run()
    mlflow.log_param("n_estimators", 100)
    mlflow.log_metric("accuracy", model.score(X_test, y_test))
    mlflow.sklearn.log_model(model, "model")
    mlflow.end_run()

if __name__ == "__main__":
    data_path = 'F:\Learning\AI\MLOps\learning_mlops\data\processed\processed_data.csv'
    train_model(data_path)
