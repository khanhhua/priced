import json

from tornado.web import RequestHandler
from tornado.template import Loader

from app import models


class InquiryHandler(RequestHandler):

    pass


class AuthHandler(RequestHandler):

    def get(self):
        self.write("Hello, world")


class RestHandler(RequestHandler):

    def __init__(self, applicationn, request, **settings):
        super(RestHandler, self).__init__(applicationn, request, **settings)

        self.set_header("Content-Type", "application/json")
        
    @property
    def db_session(self):
        return self.application.db_session
        
    def json(self, response):
        self.write(json.dumps(response))


class ProductsHandler(RestHandler):

    def get(self, product_id=None):
        if product_id:
            product = self.db_session.query(models.Product).get(product_id)
            
            self.json(dict(product=product.to_dict()))
        else:
            productQuery = self.db_session.query(models.Product)
            
            self.json(dict(products=[item.to_dict() for item in productQuery]))
            
    def post(self, *path_args, **kwargs):
        try:
            data = json.loads(self.request.body.decode("utf8"))
            product = models.Product(**data)
            
            self.db_session.add(product)
            self.db_session.commit()
            
            self.json(dict(product=product.to_dict()))
        except Exception as e:
            self.db_session.rollback()
            self.send_error(400, reason=str(e))


class UnitsHandler(RequestHandler):

    def get(self, unit_id=None):
        unit = dict(id="ID001",
                    name="Kilogram")
        if unit_id:
            self.write(json.dumps(dict(unit=unit)))
        else:
            self.write(json.dumps(dict(units=[unit])))


class TaxCodesHandler(RestHandler):

    def get(self, taxcode_id=None):
        taxcode = dict(id="ID001",
                       title="Applie")
        if taxcode_id:
            self.write(json.dumps(dict(taxcode=taxcode)))
        else:
            self.write(json.dumps(dict(taxcodes=[taxcode])))


class ClientsHandler(RequestHandler):

    def get(self):
        self.write("Hello Clients")


class UsersHandler(RequestHandler):

    def get(self):
        self.write("Hello Users")


class PageHandler(RequestHandler):

    def __init__(self, application, request, template_name=None):
        super(PageHandler, self).__init__(application, request)
        if template_name and template_name[-5:] is not ".html":
            template_name += ".html"
        self.template_name = template_name

    def get(self, matched_part=None):
        if self.template_name:
            self.render(self.template_name)
            return

        if matched_part is None:
            self.render("public/index.html")
        else:
            template_name = matched_part + ".html"
            self.render(template_name)