from app import create_app, authentication
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


def test_authorized_request(client):
    @authentication
    def mock_authentication():
        return "Success", 200

    headers = {'Authorization': 'myKey23'}

    response = client.post('/authorize', headers=headers)

    assert response.status_code == 200
    assert "Success" in response.data.decode('utf-8')
