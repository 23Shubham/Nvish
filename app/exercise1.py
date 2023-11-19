from flask import Blueprint

exercise1_app = Blueprint('exercise1', __name__)


@exercise1_app.route('/')
def index_page():
    return "Response from Server"


@exercise1_app.route('/ping', endpoint='ping_test')
def ping_server():
    return "Response from Server for api ping"
