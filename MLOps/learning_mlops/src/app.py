from flask import Flask, request, jsonify
import mlflow.pyfunc
import pandas as pd  # Don't forget to import pandas

app = Flask(__name__)

# Load model from the mounted directory
model_uri = "file:///app/mlruns/0/188638436f95465b8238bc53efe2bdd9/artifacts/model"
model = mlflow.pyfunc.load_model(model_uri)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    prediction = model.predict(pd.DataFrame(data))
    return jsonify(prediction.tolist())

if __name__ == '__main__':
    app.run(debug=True)
