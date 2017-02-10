import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from sqlalchemy import create_engine
from app.models import Base

DB_URL = os.getenv("DB_URL", None) or "postgresql://postgres:postgres@localhost/priced"
engine = create_engine(DB_URL, echo=True)

Base.metadata.create_all(engine)