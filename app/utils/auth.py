from flask import request

pre_shared_key = "myKey23"


def authorize_request(func):
    def check_auth(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return "Failure", 401
        if auth_header == pre_shared_key:
            return func(*args, *kwargs)
        else:
            return "Failure", 401

    return check_auth
