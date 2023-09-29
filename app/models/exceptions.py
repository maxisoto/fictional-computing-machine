from flask import jsonify

class CustomException(Exception):

    def __init__(self, status_code, name = "Custom Error", description = 'Error'): 
        super().__init__()
        self.description = description
        self.name = name
        self.status_code = status_code

    def get_response(self):
        response = jsonify({
            'error': {
                'code': self.status_code,
                'name': self.name,
                'description': self.description,
            }
        })
        response.status_code = self.status_code
        return response
    
class UserNotFound(Exception):

    def __init__(self, status_code, name="User Error", description = 'Error'):
        super().__init__()
        self.description = description
        self.name = name
        self.status_code = status_code
        #self.status_code = 401

    def get_response(self):
        response = jsonify({
            'error': {
                'code': self.status_code,
                'name': self.name,
                'description': self.description,
            }
        })
        response.status_code = self.status_code
        return response
    
class DatabaseError(Exception):

    def __init__(self, status_code, name="DataBase Error", description = 'Error'):
        super().__init__()
        self.description = description
        self.name = name
        self.status_code = status_code
        #self.status_code = 500

    def get_response(self):
        response = jsonify({
            'error': {
                'code': self.status_code,
                'name': self.name,
                'description': self.description,
            }
        })
        response.status_code = self.status_code
        return response

class ServerNotFound(Exception):

    def __init__(self, status_code, name="Server Error", description = 'Error'):
        super().__init__()
        self.description = description
        self.name = name
        self.status_code = status_code
        #self.status_code = 500

    def get_response(self):
        response = jsonify({
            'error': {
                'code': self.status_code,
                'name': self.name,
                'description': self.description,
            }
        })
        response.status_code = self.status_code
        return response
    
class InvalidDataError(Exception):

    def __init__(self, status_code, name="Data Error", description = 'Error'):
        super().__init__()
        self.description = description
        self.name = name
        self.status_code = status_code
        #self.status_code = 500

    def get_response(self):
        response = jsonify({
            'error': {
                'code': self.status_code,
                'name': self.name,
                'description': self.description,
            }
        })
        response.status_code = self.status_code
        return response
    