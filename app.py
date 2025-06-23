from flask import Flask, render_template, request
import os
import numpy as np
import pandas as pd
from src.DataScience.pipeline.predictions_pipeline import PredictionPipeline

app = Flask(__name__)

@app.route('/', methods=['GET'])  
def homepage():
    return render_template('index.html')

@app.route('/train', methods=["GET"]) 
def training():
    os.system("python main.py")
    return "Training Successful"

@app.route('/predict', methods=['POST']) 
def predict():
    try:
        # Collect form data from request
        data = {
            "fixed acidity": float(request.form["fixed_acidity"]),
            "volatile acidity": float(request.form["volatile_acidity"]),
            "citric acid": float(request.form["citric_acid"]),
            "residual sugar": float(request.form["residual_sugar"]),
            "chlorides": float(request.form["chlorides"]),
            "free sulfur dioxide": float(request.form["free_sulfur_dioxide"]),
            "total sulfur dioxide": float(request.form["total_sulfur_dioxide"]),
            "density": float(request.form["density"]),
            "pH": float(request.form["pH"]),
            "sulphates": float(request.form["sulphates"]),
            "alcohol": float(request.form["alcohol"]),
        }

        input_df = pd.DataFrame([data])

        # Run prediction
        pipeline = PredictionPipeline()
        result = pipeline.predict(input_df)

        # Return result 
        return render_template('index.html', prediction_text=f"Predicted Quality: {result[0]}")

    except Exception as e:
        return f"Error during prediction: {str(e)}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
