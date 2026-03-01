from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)
model = joblib.load("energy_forecast_model.pkl")

@app.route("/")
def home():
    return "Energy Forecasting API is running!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    hour = data["hour"]
    day = data["day"]

    input_data = pd.DataFrame([[hour, day]], columns=["hour", "day"])
    prediction = model.predict(input_data)

    return jsonify({"predicted_energy": float(prediction[0])})

if __name__ == "__main__":
    app.run(debug=True)