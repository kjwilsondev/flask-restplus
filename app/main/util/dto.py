# Data transfer object (DTO)
# Responsible for carrying data between processes
# Used for marshaling data for our API calls

from flask_restplus import Namespace, fields

class UserDto:
    # create a new namespace for user related operations
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'public_id': fields.String(description='user Identifier')
    })
