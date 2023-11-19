from app import create_app
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


def test_ping_server(client):
    response = client.get('/ping')
    assert response.status_code == 200

    assert 'Response from Server for api ping' in response.data.decode('utf-8')
