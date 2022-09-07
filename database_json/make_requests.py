import requests
import json


#GET request-------------------------------------------------
url = 'http://127.0.0.1:8000/api/v1/database'

parameters = {
    "indexes": "1,2,4"
}

response = requests.get(url, params=parameters)
print(response.status_code)
print(response.json())
print()

