from app import create_app
import json
from app import authentication
# from app.DAO import close_db
import pytest


@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    yield app


@pytest.fixture
def client(app):
    with app.test_client() as client:
        yield client


def test_save_api(client):
    # app = create_app()
    # app.config['TESTING'] = True
    # client = app.test_client()

    data = {'key': 'test_key', 'value': 'test_value'}
    response = client.post('/save', json=data)
    assert response.status_code == 200
    assert 'added successfully' in response.data.decode('utf-8')


def test_get_api(client):
    # app = create_app()
    # app.config['TESTING'] = True
    # client = app.test_client()

    response = client.get('/get')
    assert response.status_code == 200
    data = json.loads(response.data.decode('utf-8'))
    assert isinstance(data, list)


def test_ping_api(client):
    response = client.get('/ping')
    assert response.status_code == 200


def test_authorized_request(client):
    @authentication
    def mock_authentication():
        return "Success", 200

    headers = {'Authorization': 'myKey23'}

    response = client.post('/authorize', headers=headers)

    assert response.status_code == 200
    assert "Success" in response.data.decode('utf-8')
