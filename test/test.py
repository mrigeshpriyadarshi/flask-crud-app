import os
import requests
import json

url = "http://ec2-54-162-25-216.compute-1.amazonaws.com:5000"
# response = requests.get(url + "/api/v1/listusers")
# print(response.json())

# response = requests.get(url + "/api/v1/listuser/007")
# print(response.json())


# headers = {"Content-Type": "application/json"}
# param = {'customer_id': "007", 'email': "mrig@dbs.com", 'name': 'pra', 'pwd': "abc"}
# response = requests.put(url + "/api/v1/update/007", data=json.dumps(param), headers=headers)
# print(response.json())

headers = {"Content-Type": "application/json"}
param = {'customer_id': "007", 'email': "mrig@dbs.com", 'name': 'pra', 'pwd': "abc"}
response = requests.delete(url + "/api/v1/delete/007")
print(response.json())