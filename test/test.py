import os
import requests
import json

url = "http://ec2-54-162-25-216.compute-1.amazonaws.com:5000"
0

# response = requests.get(url + "/api/v1/listuser/007")
# print(response.json())
url = "http://127.0.0.1:5000"


headers = {"Content-Type": "application/json"}
param = {'customer_id': "007", 'email': "mrig@dbs.com", 'name': 'pra', 'surname': "abc"}
response = requests.put(url + "/api/v1/adduser", data=json.dumps(param), headers=headers)
print(response.json())

headers = {"Content-Type": "application/json"}
param = {'customer_id': "007", 'email': "mrig@dbs.com", 'name': 'pra', 'pwd': "abc"}
response = requests.delete(url + "/api/v1/delete/007")
print(response.json())