import pytest
from app import createApp

@pytest.fixture
def app():
    app = createApp()
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

