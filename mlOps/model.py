import json
import requests
from flask import Flask, request, jsonify
from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.classification import DecisionTreeClassifier
from pyspark.ml.evaluation import MulticlassClassificationEvaluator

spark = SparkSession.builder.appName("DTmodel").getOrCreate()

df = spark.read.csv("/home/bhavesh/Downloads/predictive_maintenance.csv", header=True, inferSchema=True)

columns_to_drop = ["UDI", "Product ID", "Type", "Failure Type"]
df = df.drop(*columns_to_drop)

feature_columns = df.columns[:-1]
assembler = VectorAssembler(inputCols=feature_columns, outputCol="features")
df = assembler.transform(df)

(training_data, test_data) = df.randomSplit([0.7, 0.3])

dt = DecisionTreeClassifier(labelCol="Target", featuresCol="features")
dt_model = dt.fit(training_data)

# Initialize Flask app
app = Flask(__name__)

# Define a route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get JSON data from the request
        df_from_json = spark.read.json(spark.sparkContext.parallelize(request.json))

        assembler = VectorAssembler(inputCols=["Air temperature [K]","Process temperature [K]","Rotational speed [rpm]","Torque [Nm]","Tool wear [min]"], outputCol="features")
        df_from_json = assembler.transform(df_from_json)

        # Make predictions using the model
        predictions = dt_model.transform(df_from_json)

        predictions.select("prediction").show()

        return jsonify({"predictions": "hi"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the Flask app on port 8001
if __name__ == '__main__':
    app.run(debug=True, port=8001)