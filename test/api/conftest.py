import pytest

@pytest.fixture(scope="session")
def app():
    from wsgi import application

    return application
