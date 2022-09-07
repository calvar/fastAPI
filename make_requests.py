import requests
import json


#GET request----------------------------------------------------
url = "http://127.0.0.1:8000/api/v1/users"

response = requests.get(url)
print(response.status_code)
print(response.json())
print()

#POST request----------------------------------------------------
#load user information
In = open("new_user.json")
new_user = json.load(In)
In.close()
#convert to string
contents = json.dumps(new_user)
url = "http://127.0.0.1:8000/api/v1/users"

response = requests.post(url, data=contents)
print(response.status_code)
print(response.json())
print()

#Another GET request--------------------------------------------
url = "http://127.0.0.1:8000/api/v1/users"

response = requests.get(url)
print(response.status_code)
print(response.json())
print()

#DELETE request-------------------------------------------------
#Get last user id
uid = response.json()[len(response.json())-1]["id"]
url = "http://127.0.0.1:8000/api/v1/users/"+str(uid)

response = requests.delete(url)
print(response.status_code)
print(response.json())
print()

#Another GET request--------------------------------------------
url = "http://127.0.0.1:8000/api/v1/users"

response = requests.get(url)
print(response.status_code)
print(response.json())
print()

#PUT request---------------------------------------------------
#Get first user id
uid = response.json()[0]["id"]
#load user update information
In = open("update_user.json")
update_user = json.load(In)
In.close()
#convert to string
contents = json.dumps(update_user)
url = "http://127.0.0.1:8000/api/v1/users/"+str(uid)

response = requests.put(url, data=contents)
print(response.status_code)
print(response.json())
print()

#Another GET request--------------------------------------------
url = "http://127.0.0.1:8000/api/v1/users"

response = requests.get(url)
print(response.status_code)
print(response.json())
print()
