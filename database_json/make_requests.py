import requests
import json


#GET request-------------------------------------------------
url = 'http://127.0.0.1:8000/api/v1/database'

parameters = {
    "indexes": "2,4"
}

response = requests.get(url, params=parameters)
print(response.status_code)
print(response.json())
print()

#POST request------------------------------------------------
url = 'http://127.0.0.1:8000/api/v1/database'

new_data = [
    {"C1": 10, "C2": "b", "C3": 2.3},
    {"C1": 8, "C2": "b", "C3": 2.5}
]
contents = json.dumps(new_data)

response = requests.post(url, data=contents)
print(response.status_code)
print(response.json())
print()

#GET request-------------------------------------------------
url = 'http://127.0.0.1:8000/api/v1/database'

parameters = {
    "indexes": ""
}

response = requests.get(url, params=parameters)
print(response.status_code)
print(response.json())
print()
