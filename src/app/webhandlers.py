from tornado.web import RequestHandler
from tornado.template import Loader


class InquiryHandler(RequestHandler):

    pass


class AuthHandler(RequestHandler):

    def get(self):
        self.write("Hello, world")


class ProductsHandler(RequestHandler):

    def get(self):
        self.write("Hello Products")


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

    def __init__(self, application, request, file_path):
        super(PageHandler, self).__init__(application, request)

        self.file_path = file_path

    def get(self, matched_part=None):
        if self.file_path:
            self.render(self.file_path)
            return

        if matched_part is None:
            self.render("public/index.html")
        else:
            template_name = matched_part + ".html"
            self.render(template_name)