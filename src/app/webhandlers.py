import json

from tornado.web import RequestHandler


class InquiryHandler(RequestHandler):

    pass


class AuthHandler(RequestHandler):

    def get(self):
        self.write("Hello, world")


class RestHandler(RequestHandler):

    def __init__(self, applicationn, request, **settings):
        super(RestHandler, self).__init__(applicationn, request, **settings)

        self.set_header("Content-Type", "application/json")


class ProductsHandler(RestHandler):

    def get(self, product_id=None):
        product = dict(id="ID001",
                       name="Applie")
        if product_id:
            self.write(json.dumps(dict(product=product)))
        else:
            self.write(json.dumps(dict(products=[product])))


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
        taxcode_body = """EACH item
            TAX item
        """

        taxcode = dict(id="ID001",
                       created_at="2017-01-01T06:00:00Z",
                       effective_at="2017-01-01T06:00:00Z",
                       expired_at="2017-01-31T06:00:00Z",
                       title="Apple",
                       shared=True,
                       body=taxcode_body)
        if taxcode_id:
            self.write(json.dumps(dict(taxcode=taxcode)))
        else:
            self.write(json.dumps(dict(taxcodes=[taxcode])))


class ScenariosHandler(RestHandler):

    def get(self, scenario_id=None):
        description = """
        Banana      1kg
        Orange      2kg
        Apple       4kg
        ====
        Shipping
        """.strip()

        scenario = dict(id="ID001",
                        description=description)
        if scenario_id:
            self.write(json.dumps(dict(scenario=scenario)))
        else:
            self.write(json.dumps(dict(scenarios=[scenario])))


class ScenarioSessionsHandler(RestHandler):

    def post(self, *path_args, **kwargs):
        body = self.request.body
        data = json.loads(body.decode("utf8"))

        self.write("\"ok\"")


class TransactionsHandler(RestHandler):

    def post(self, *path_args, **kwargs):
        body = self.request.body
        data = json.loads(body.decode("utf8"))

        # Input data should contain
        # 1. Lines of product purchased (quantity, unit)
        # 2. Additional services
        # 3. Dates of transaction
        #
        # Output data
        # 1. Lines of product with quantity, price, unit
        # 2. Total amount due with details about tax and price before tax

        self.write("\"ok\"")


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