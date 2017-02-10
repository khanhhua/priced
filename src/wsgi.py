import sys, os
from os.path import (join,
                     dirname,
                     realpath)

from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker

from tornado.web import (StaticFileHandler,
                         Application,
                         url
                         )

base_path = dirname(__file__)
sys.path.insert(0, base_path)

static_path   = realpath(join(base_path, "static", "assets"))
template_path = realpath(join(base_path, "template"))

print("template_path: %s" % template_path)
print("static_path: %s" % static_path)

from app import webhandlers
urls = [url(r"/", webhandlers.PageHandler),
        url(r"/admin(/.*)?", webhandlers.PageHandler, {"template_name": "admin/index"}),
        url(r"/api/products(?:/(.+))?", webhandlers.ProductsHandler),
        url(r"/api/taxcodes(?:/(.+))?", webhandlers.TaxCodesHandler),
        url(r"/api/units(?:/(.+))?", webhandlers.UnitsHandler)
        ]
# url(r"/api/products/(?P<product_id>)")

config = dict(static_url_prefix="/assets/",
              static_path=static_path,
              template_path=template_path,
              debug=True,
              autoreload=True)
              
class App(Application):
    
    def __init__(self, urls, **kwargs):
        super(App, self).__init__(urls, **kwargs)
        self._db_session = None
    
    @property
    def db_session(self):
        if self._db_session:
            return self._db_session
        
        DB_URL = os.getenv("DB_URL", None) or "postgresql://postgres:postgres@localhost/priced"
        engine = create_engine(DB_URL, echo=True)
        
        session = sessionmaker()
        session.configure(bind=engine)
        
        self._db_session = session()
        return self._db_session

        
application = App(urls, **config)

if __name__ == "__main__":
    application.listen(os.getenv("PORT", 8080))

    import tornado.ioloop
    tornado.ioloop.IOLoop().current().start()