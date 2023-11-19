from flask import Flask
import flask_caching
from app.utils.auth import authorize_request

app = Flask(__name__)

cache = flask_caching.Cache(app, config={'CACHE_TYPE': 'simple'})

authentication = authorize_request


def register_blueprints():
    from app.exercise1 import exercise1_app
    app.register_blueprint(exercise1_app)

    from app.exercise2 import exercise2_app
    app.register_blueprint(exercise2_app)

    from app.exercise3 import exercise3_app
    app.register_blueprint(exercise3_app)


register_blueprints()


def create_app():
    with app.app_context():
        from .models import create_database
        create_database()
    return app
