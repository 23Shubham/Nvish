from flask import Blueprint
from app import authentication

exercise2_app = Blueprint('exercise2', __name__)


@exercise2_app.route('/authorize', methods=['POST'], endpoint='authorize_test')
@authentication
def authorized_request():
    return "Success", 200
