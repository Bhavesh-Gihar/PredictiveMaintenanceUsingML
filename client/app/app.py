import json
import pickle
import requests
import numpy as np
from sklearn.linear_model import LinearRegression

with open('/home/bhavesh/Documents/PredictiveMaintenanceUsingML/client/app/model.pkl', 'rb') as f:
    tinymlModel = pickle.load(f)

# Input data
input_data = {
    # "UDI": "1",
    # "Product ID": "M14860",
    # "Type": "M",
    # "Air temperature [K]": "298.1",
    # "Process temperature [K]": "308.6",
    # "Rotational speed [rpm]": "1551",
    # "Torque [Nm]": "42.8",
    # "Tool wear [min]": "0",
    # "Failure Type": "No Failure"

    "data": [[70,"L47341","L",298.9,309.0,1410,65.7,191], 
             [162,"L47341","L",298.3,308.1,1412,52.3,218], 
             [169,"L47341","L",298.4,308.3,1433,62.3,20]]
}

data_array = np.array(input_data['data'])
processed_data = data_array[:, 3:]
processed_data = [np.array(i, dtype=float) for i in processed_data]

predictions = tinymlModel.predict(processed_data)

count = 0
for i in predictions:
    if(i > 0.02):
        count = count + 1

if(count > len(predictions)/2):
    # URL of the Flask backend
    url = "http://127.0.0.1:5000/predict"

    json_string = json.dumps(input_data)

    # Send a POST request with the input
    response = requests.post(url, json=json_string)

    # Check the response
    if response.status_code == 200:
        print("POST request successful")
    else:
        print("POST request failed with status code:", response.text)
