import json
import boto3
import requests
import mysql.connector
from flask import Flask, request, jsonify
from pyspark.sql import SparkSession
from pyspark.ml import PipelineModel

app = Flask(__name__)

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("FlaskSparkIntegration") \
    .getOrCreate()

# Initialize SQL connector
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="predictiveMaintenance",
    auth_plugin="mysql_native_password",
)

# Initialize the SNS client
sns_client = boto3.client('sns', region_name='ap-south-1')

# Specify the ARN of the SNS topic you want to publish to
topic_arn = 'arn:aws:sns:ap-south-1:905418023525:PredictiveMaintenanceUsingMLsns'

# insert = [
#     """insert into predictiveMaintenance values (1,'M14860','M',298.1,308.6,1551,42.8,0,0);"""
# ]

# cursor = db.cursor()
# for i in insert:
#     cursor.execute(i)

# db.commit()

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get JSON data from the request
        data = json.loads(request.json)
        
        # Preprocess data using Apache Spark
        columns = ["UDI","Product ID","Type","Air temperature [K]","Process temperature [K]","Rotational speed [rpm]","Torque [Nm]","Tool wear [min]"]
        df = spark.createDataFrame(data['data'], columns)

        print("Input data received !!")
        
        # # Preprocess your data using Spark pipelines or other transformations
        columns_to_drop = ["UDI", "Product ID", "Type"]
        df = df.drop(*columns_to_drop)

        print("Input data processed !!")

        # URL of the Flask backend
        url = "http://127.0.0.1:8001/predict"

        # Convert DataFrame to JSON string
        json_string = df.toJSON().collect()

        # Send a POST request
        response = requests.post(url, json=json_string)
        responseData = json.loads(response.text)

        print("Predictions received !!")
        
        # # Convert predictions to a list
        # result = [row["prediction"] for row in predicted_data]
        # print(response.text)

        # return jsonify({"predictions": response.text})

        cursor = db.cursor()
        for idx, i in enumerate(data['data']):
            insertQuery = f"""insert into predictiveMaintenance values ({i[0]},\'{i[1]}\',\'{i[2]}\',{i[3]},{i[4]},{i[5]},{i[6]},{i[7]},{responseData['predictions'][idx]});"""
            print(insertQuery)
            cursor.execute(insertQuery)
        db.commit()

        print("Committed to database !!")

        count = 0
        for i in responseData['predictions']:
            if(i == 1):
                count = count + 1
        if(count > len(responseData['predictions'])/2):
            message = f"Fault predicted on Product {data['data'][0][1]} !!"
            response = sns_client.publish(
                TopicArn=topic_arn,
                Message=message
            )
        
        print("Message sent !!")

        return jsonify({"Request": "Success"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500