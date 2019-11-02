import os
import sys
from bson.json_util import dumps
import connection

def openc():
	return connection.get()

def close(client):
	return connection.close(client)

def get_collection(client):
	##Specify the database to be used
	db = client.flaskapp
	##Specify the collection to be used
	return db.myTestCollection

def get_data():
	try:
		client = openc()
		data = get_collection(client).find()
		close(client)
	except Exception as e:
		raise e
	else:
		return data

def get_customer_list():
	customer_list = []
	for data in get_data():
		customer_list.append(data['_id'])
	return get_customer_list

def get_customer(customer_id):
	try:
		client = openc()
		data = get_collection(client).find_one({"_id": customer_id})
		close(client)
	except Exception as e:
		raise e
	else:
		return data

def update(data):
	try:
		client = openc()
		result = get_collection(client).update({"_id": data['customer_id']}, data)
		close(client)
	except Exception as e:
		raise e
	else:
		return result


def add(data):
	try:
		client = openc()
		result = get_collection(client).insert_one(data)
		close(client)
	except Exception as e:
		raise e
	else:
		return result

def delete(customer_id):
	try:
		client = openc()
		result = get_collection(client).delete_one({"_id": customer_id})
		close(client)
	except Exception as e:
		raise e
	else:
		return result

