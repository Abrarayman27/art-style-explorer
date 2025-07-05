from flask import Flask, request, jsonify
import joblib
import os
import numpy as np
from database import log_prediction

app = Flask(__name__)

# Load the model
model_path = "/app/model/iris_decision_tree.joblib"
if not os.path.exists(model_path):
    raise FileNotFoundError("Model file not found")
model = joblib.load(model_path)

# Define class names for Iris dataset
class_names = ["setosa", "versicolor", "virginica"]

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Iris Prediction API"})

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get JSON data from request
        data = request.get_json()
        if not data:
            return jsonify({"error": "No input data provided"}), 400

        # Validate input
        required_fields = ["sepal_length", "sepal_width", "petal_length", "petal_width"]
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing field: {field}"}), 400

        # Prepare input data
        input_data = np.array([[
            data["sepal_length"],
            data["sepal_width"],
            data["petal_length"],
            data["petal_width"]
        ]])

        # Make prediction
        prediction = model.predict(input_data)[0]
        predicted_class = class_names[int(prediction)]

        # Log prediction to database
        log_prediction(
            sepal_length=data["sepal_length"],
            sepal_width=data["sepal_width"],
            petal_length=data["petal_length"],
            petal_width=data["petal_width"],
            prediction=predicted_class
        )

        return jsonify({"prediction": predicted_class})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)