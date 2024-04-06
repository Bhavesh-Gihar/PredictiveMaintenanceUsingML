import json
import requests
from flask import Flask, request, jsonify
from pyspark.sql import SparkSession
from pyspark.ml import PipelineModel

app = Flask(__name__)

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("FlaskSparkIntegration") \
    .getOrCreate()

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get JSON data from the request
        data = json.loads(request.json)
        
        # Preprocess data using Apache Spark
        columns = ["UDI","Product ID","Type","Air temperature [K]","Process temperature [K]","Rotational speed [rpm]","Torque [Nm]","Tool wear [min]"]
        df = spark.createDataFrame(data['data'], columns)
        
        # # Preprocess your data using Spark pipelines or other transformations
        columns_to_drop = ["UDI", "Product ID", "Type"]
        df = df.drop(*columns_to_drop)

        # URL of the Flask backend
        url = "http://127.0.0.1:8001/predict"

        # Convert DataFrame to JSON string
        json_string = df.toJSON().collect()

        # Send a POST reques
        response = requests.post(url, json=json_string)
        
        # # Convert predictions to a list
        # result = [row["prediction"] for row in predicted_data]

        return jsonify({"predictions": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500