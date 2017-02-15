import pytest

@pytest.fixture(scope="session")
def app():
    import os
    from sqlalchemy import create_engine
    from wsgi import application
    from app.models import Base
    
    DB_URL = os.getenv("DB_URL", None) or "postgresql://postgres:postgres@localhost/priced-test"
    engine = create_engine(DB_URL, echo=True)
    
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    return application
