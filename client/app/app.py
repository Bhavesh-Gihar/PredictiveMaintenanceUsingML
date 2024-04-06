import requests
import json

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

    "data": [[1,"M14860","M",298.1,308.6,1551,42.8,0], 
             [162,"L47341","L",298.3,308.1,1412,52.3,218], 
             [169,"L47348","L",298.4,308.3,1433,62.3,20]]
}

# URL of the Flask backend
url = "http://127.0.0.1:5000/predict"

json_string = json.dumps(input_data)

# Send a POST request with the random JSON object
response = requests.post(url, json=json_string)

# Check the response
if response.status_code == 200:
    print("POST request successful")
    print("Response:")
    print(response.json())
else:
    print("POST request failed with status code:", response.text)
