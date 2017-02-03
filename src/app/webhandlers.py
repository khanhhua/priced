from tornado.web import RequestHandler


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