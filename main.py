from app import app
from bson.json_util import dumps
from flask import jsonify, request
from flask import flash, render_template, redirect
import logging
import settings
from tables import Results
import json
import os

from lib import db

logging.basicConfig(level=logging.DEBUG, filename=os.environ['log_dir'] + '/server.log', datefmt='%I:%M:%S %p',)


@app.route('/new_user')
def add_user_view():
	return render_template('add.html')


@app.route('/add', methods=['POST'])
def add_user():
	customer_id = request.form['customerId']
	name = request.form['inputName']
	email = request.form['inputEmail']
	surname = request.form['inputSurname']
	# validate the received values
	if name and email and surname and request.method == 'POST':
		# save details
		id = db.add({'_id': customer_id, 'name': name, 'email': email, 'surname': surname})
		flash('User added successfully!')
		return redirect('/')
	else:
		return not_found()
		
@app.route('/')
def users():
	try:
		rows = db.get_data()
		table = Results(rows)
		table.border = True
		return render_template('users.html', table=table)
	except Exception as e:
		print(e)
		
@app.route('/user/<customer_id>')
def user(customer_id):
	user = db.get_customer(customer_id)
	resp = dumps(user)
	return resp


@app.route('/edit/<id>')
def edit_view(id):
	try:
		row = db.get_customer(id)
		if row:
			return render_template('update.html', row=row)
		else:
			return 'Error loading #{customer_id}'.format(customer_id=id)
	except Exception as e:
		print(e)


@app.route('/update', methods=['POST'])
def update_user():
	customer_id = request.form['customerId']
	name = request.form['inputName']
	email = request.form['inputEmail']
	surname = request.form['inputSurname']

	# validate the received values
	try:
		if name and email and surname and customer_id and request.method == 'POST':
			# save edits
			db.update({'customer_id': customer_id, 'name': name, 'email': email, 'surname': surname})
			flash('User updated successfully!')
			return redirect('/')
		else:
			return not_found()
	except Exception as e:
		print(e)


		
@app.route('/delete/<id>')
def delete_user(id):
	db.delete(id)
	flash('User deleted successfully!')
	return redirect('/')


@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp


# API SECTION

@app.route('/api/v1/adduser')
def api_add_user():
        _json = request.json
        customer_id = _json['customer_id']
        name = _json['name']
        email = _json['email']
        surname = _json['surname']
        # validate the received values
        if name and email and password and request.method == 'POST':
            # save details
            id = db.add({'customer_id': customer_id, 'name': name, 'email': email, 'surname': surname})
            resp = jsonify('User added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found()


@app.route('/api/v1/listusers')
def api_get_users():
        try:
                rows = db.get_data()
                resp = dumps(rows, indent=4)
                # resp = json.dumps(rows, indent=4)
                return resp
        except Exception as e:
                print(e)

@app.route('/api/v1/listuser/<customer_id>')
def api_get_user(customer_id):
        try:
                user = db.get_customer(customer_id)
                resp = dumps(rows, indent=4)
                # resp = json.dumps(user, indent=4)
                return resp
        except Exception as e:
                print(e)

@app.route('/api/v1/update/<customer_id>', methods=['PUT'])
def api_update_user(customer_id):
    try:
        _json = request.json
        customer_id = _json['customer_id']
        name = _json['name']
        email = _json['email']
        surname = _json['surname']
        # validate the received values
        if name and email and surname and customer_id and request.method == 'PUT':
            # save edits
            db.update({'customer_id': customer_id, 'name': name, 'email': email, 'surname': surname})
            resp = jsonify('User updated successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)
        print("in update")

@app.route('/api/v1/delete/<customer_id>', methods=['DELETE'])
def api_delete_user(customer_id):
	db.delete(customer_id)
	resp = jsonify('User deleted successfully!')
	resp.status_code = 200
	return resp

if __name__ == "__main__":
    app.run(host='0.0.0.0')