import json
from datetime import datetime

from tornado.web import RequestHandler

from app import models


class InquiryHandler(RequestHandler):

    pass


class AuthHandler(RequestHandler):

    def get(self):
        self.write("Hello, world")


class RestHandler(RequestHandler):

    def __init__(self, applicationn, request, **settings):
        super(RestHandler, self).__init__(applicationn, request, **settings)
        
        self._db_session = None
        self.set_header("Content-Type", "application/json")
        
    @property
    def db_session(self):
        if self._db_session:
            return self._db_session
        
        self._db_session = self.application.db_session()
        return self._db_session
        
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
            data['id'] = self.application.hashid()
            data['kind'] = 'generic'

            product = models.Product(**data)
            
            self.db_session.add(product)
            self.db_session.commit()
            
            self.json(dict(product=product.to_dict()))
        except Exception as e:
            self.db_session.rollback()
            self.send_error(400, reason=str(e))


class ProductPricesHandler(RestHandler):

    def get(self, product_id, price_id=None):
        product = self.db_session.query(models.Product).get(product_id)

        if price_id:
            price_query = (self.db_session.query(models.Price)
                          .filter(models.Price.id==price_id))
            price = price_query.one()
            self.json(dict(price=price.to_dict()))
        else:
            self.json(dict(prices=[item.to_dict() for item in product.pricings]))

    def post(self, product_id, *path_args, **kwargs):
        product = self.db_session.query(models.Product).get(product_id)

        try:
            data = json.loads(self.request.body.decode("utf8"))
            data["id"] = self.application.hashid()
            data["created_at"] = datetime.utcnow()
            data["product"] = product

            price = models.Price(**data)
            self.db_session.add(price)
            self.db_session.commit()

            self.json(dict(price=price.to_dict()))
        except Exception as e:
            self.db_session.rollback()
            self.send_error(400, reason=str(e))


class UnitsHandler(RestHandler):

    def get(self, unit_id=None):
        if unit_id:
            unit = self.db_session.query(models.Unit).get(unit_id)
            
            self.write(json.dumps(dict(unit=unit.to_dict())))
        else:
            unit_query = self.db_session.query(models.Unit)
            
            self.write(json.dumps(dict(units=[unit.to_dict() for unit in unit_query])))
            
    def post(self, *path_args, **kwargs):
        try:
            data = json.loads(self.request.body.decode("utf8"))
            data["id"] = self.application.hashid()
            data["created_at"] = datetime.utcnow()
            
            unit = models.Unit(**data)
            self.db_session.add(unit)
            self.db_session.commit()
            
            self.json(dict(unit=unit.to_dict()))
        except Exception as e:
            self.db_session.rollback()
            self.send_error(400, reason=str(e))


class TaxCodesHandler(RestHandler):

    def get(self, taxcode_id=None):
        if taxcode_id:
            taxcode = self.db_session.query(models.Taxcode).get(taxcode_id)
            self.json(dict(taxcode=taxcode.to_dict()))
        else:
            taxcode_query = self.db_session.query(models.Taxcode)
            self.json(dict(taxcodes=[item.to_dict() for item in taxcode_query]))

    def post(self, *path_args, **kwargs):
        try:
            data = json.loads(self.request.body.decode("utf8"))
            taxcode = models.Taxcode(**data)
            taxcode.id = self.application.hashid()
            taxcode.shared = False
            
            self.db_session.add(taxcode)
            self.db_session.commit()
            self.db_session.refresh(taxcode)
            
            self.json(dict(taxcode=taxcode.to_dict()))
        except Exception as e:
            self.db_session.rollback()
            self.send_error(400, reason=str(e))
            

class ScenariosHandler(RestHandler):

    def get(self, scenario_id=None):
        if scenario_id:
            scenario = self.db_session.query(models.Scenario).get(scenario_id)
            self.json(dict(scenario=scenario.to_dict()))
        else:
            scenario_query = self.db_session.query(models.Scenario)
            self.json(dict(scenarios=[scenario.to_dict() for scenario in scenario_query]))
            
    def post(self, *path_args, **kwargs):
        try:
            data = json.loads(self.request.body.decode("utf8"))
            
            scenario = models.Scenario(**data)
            scenario.id = self.application.hashid()
            self.db_session.add(scenario)
            self.db_session.commit()
            
            self.db_session.refresh(scenario)
            
            self.json(dict(scenario=scenario.to_dict()))
        except Exception as e:
            self.db_session.rollback()
            self.send_error(400, reason=str(e))


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