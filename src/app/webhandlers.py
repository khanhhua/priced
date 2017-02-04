import json

from tornado.web import RequestHandler
from tornado.template import Loader


class InquiryHandler(RequestHandler):

    pass


class AuthHandler(RequestHandler):

    def get(self):
        self.write("Hello, world")


class ProductsHandler(RequestHandler):

    def get(self, product_id=None):
        self.set_header("Content-Type", "application/json")

        product = dict(id="ID001",
                       name="Applie")
        if product_id:
            self.write(json.dumps(dict(product=product)))
        else:
            self.write(json.dumps(dict(products=[product])))


class UnitsHandler(RequestHandler):

    def get(self):
        self.write("Hello Units")


class TaxCodesHandler(RequestHandler):

    def get(self):
        self.write("Hello Tax Codes")


class ClientsHandler(RequestHandler):

    def get(self):
        self.write("Hello Clients")


class UsersHandler(RequestHandler):

    def get(self):
        self.write("Hello Users")


class PageHandler(RequestHandler):

    def __init__(self, application, request, template_name):
        super(PageHandler, self).__init__(application, request)
        if template_name[-5:] is not ".html":
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