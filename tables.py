from flask_table import Table, Col, LinkCol
 
class Results(Table):
    _id = Col('CustId')
    name = Col('Name')
    surname = Col('Surname')
    email = Col('Email')
    edit = LinkCol('Update', 'edit_view', url_kwargs=dict(id='_id'))
    delete = LinkCol('Delete', 'delete_user', url_kwargs=dict(id='_id'))