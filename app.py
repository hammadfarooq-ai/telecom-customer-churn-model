from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("model/model.pkl")

@app.route("/")
def home():
    return {"message": "Telco Churn Prediction API is running!"}

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json["data"]
    data = np.array(data).reshape(1, -1)

    prediction = model.predict(data)[0]
    return jsonify({"churn_prediction": int(prediction)})

if __name__ == "__main__":
    app.run(debug=True)
