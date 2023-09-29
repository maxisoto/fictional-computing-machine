from flask import Blueprint
from ..models.exceptions import CustomException, UserNotFound, DatabaseError, ServerNotFound, InvalidDataError


errors = Blueprint("errors", __name__)

@errors.app_errorhandler(ServerNotFound)
def handle_server_not_found(error):
    return error.get_response(), error.status_code

@errors.app_errorhandler(InvalidDataError)
def handle_invalid_data_error(error):
    return error.get_response(), error.status_code

@errors.app_errorhandler(CustomException)
def handle_custom_not_found(error):
    return error.get_response(), error.status_code

@errors.app_errorhandler(UserNotFound)
def handle_user_not_found(error):
    return error.get_response(), error.status_code

@errors.app_errorhandler(DatabaseError)
def handle_database_error(error):
    return error.get_response(), error.status_code