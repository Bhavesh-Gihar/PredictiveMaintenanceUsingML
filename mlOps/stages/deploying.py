from pyspark import *
from flask import Flask, request, jsonify
from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler


class deployer:
    def deploy(self, model):
        # Get or create Spark session
        spark = SparkSession.builder.getOrCreate()

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
                predictions = model.transform(df_from_json)

                predictions.select("prediction").show()

                return jsonify({"predictions": "hi"})
            except Exception as e:
                return jsonify({"error": str(e)}), 500
            
        return app
        
