from app import create_app
import json
from app import authentication
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
    data = {'key': 'test_key', 'value': 'test_value'}
    headers = {'Authorization': 'myKey23'}

    response = client.post('/save', json=data, headers=headers)
    assert response.status_code == 200
    assert 'added successfully' in response.data.decode('utf-8')


def test_get_api(client):
    headers = {'Authorization': 'myKey23'}
    response = client.get('/get', headers=headers)
    assert response.status_code == 200
    data = json.loads(response.data.decode('utf-8'))
    assert isinstance(data, list)


def test_delete_api(client):
    headers = {'Authorization': 'myKey23'}
    data = {'key': 'test_key'}
    response = client.post('/delete', json=data, headers=headers)
    assert response.status_code == 200
    assert "Deleted successfully" in response.data.decode('utf-8')
