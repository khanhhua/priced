import os, random

from tornado.web import Application

from hashids import Hashids

from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker

# Application variables
# DB_URL
HASHID_SALT = "secretoftheorder"

class App(Application):

    def __init__(self, urls, **kwargs):
        super(App, self).__init__(urls, **kwargs)
        self._db_session = None
        self._hashid = None

    @property
    def db_session(self):
        if self._db_session:
            return self._db_session

        DB_URL = os.getenv("DB_URL", None) or "postgresql://postgres:postgres@localhost/priced"
        engine = create_engine(DB_URL, echo=True)

        self._db_session = sessionmaker()
        self._db_session.configure(bind=engine)

        return self._db_session

    def hashid(self, num=None):
        if num is None:
            # 0.0684348973943405
            num = int(random.random() * 1e16)

        if self._hashid:
            return self._hashid.encode(num)

        self._hashid = Hashids(salt=HASHID_SALT,
                               min_length=16)
        return self._hashid.encode(num)