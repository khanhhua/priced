import sys
from os.path import (join,
                     dirname,
                     realpath)
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
        url(r"/api/transactions", webhandlers.TransactionsHandler),
        url(r"/api/products(?:/(.+))?", webhandlers.ProductsHandler),
        url(r"/api/taxcodes(?:/(.+))?", webhandlers.TaxCodesHandler),
        url(r"/api/units(?:/(.+))?", webhandlers.UnitsHandler),
        url(r"/api/scenarios(?:/(.+))?", webhandlers.ScenariosHandler),
        url(r"/api/scenario-sessions(?:/(.+))?", webhandlers.ScenarioSessionsHandler)
        ]
# url(r"/api/products/(?P<product_id>)")

config = dict(static_url_prefix="/assets/",
              static_path=static_path,
              template_path=template_path,
              debug=True,
              autoreload=True)
application = Application(urls, **config)

if __name__ == "__main__":
    application.listen(8888)

    import tornado.ioloop
    tornado.ioloop.IOLoop().current().start()