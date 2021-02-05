import requests
import json

# URL for the web service, should be similar to:
scoring_uri = 'http://bb4efe9e-b384-4e1f-8924-6098a665238f.southcentralus.azurecontainer.io/score'
# If the service is authenticated, set the key or token
key = 'K7t6k5pM27WGrnwVrCT9hhGa9BhWE1rk'

# Two sets of data to score, so we get two results back
data = {"data":
        [
          {
            "age": 55,
            "anaemia": 0,
            "creatinine_phosphokinase": 1199,
            "diabetes": 0,
            "ejection_fraction": 20,
            "high_blood_pressure": 0,
            "platelets": 263358.03,
            "serum_creatinine": 1.83,
            "serum_sodium": 134,
            "sex": 1,
            "smoking": 1,
            "time": 241
            },
          {
            "age": 50,
            "anaemia": 0,
            "creatinine_phosphokinase": 196,
            "diabetes": 0,
            "ejection_fraction": 45,
            "high_blood_pressure": 0,
            "platelets": 395000,
            "serum_creatinine": 1.6,
            "serum_sodium": 136,
            "sex": 1,
            "smoking": 1,
            "time": 285
          },
      ]
    }
# Convert to JSON string
input_data = json.dumps(data)
with open("data.json", "w") as _f:
    _f.write(input_data)

# Set the content type
headers = {'Content-Type': 'application/json'}
# If authentication is enabled, set the authorization header
headers['Authorization'] = f'Bearer {key}'

# Make the request and display the response
resp = requests.post(scoring_uri, input_data, headers=headers)
print(resp.json())
