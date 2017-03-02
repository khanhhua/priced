import pytest
import json

from app.models import Base, Taxcode

class TestTaxcodesApi(object):
    
    @pytest.mark.gen_test(run_sync=False)
    def test_list(self, http_client, base_url, app):
        res = yield http_client.fetch(base_url + "/api/taxcodes")
        
        assert res.code == 200
        data = json.loads(res.body.decode("utf8"))
        
        assert len(data["taxcodes"]) >= 0
        
    @pytest.mark.gen_test(run_sync=False)
    def test_create(self, http_client, base_url, app):
        taxcode_body = \
"""
TAX 10% "Tax 10% based on price"
"""
        body = json.dumps(dict(title="Test Taxcode",
                               effective_at="2017-01-01T00:00:00Z",
                               expired_at="2017-01-31T00:00:00Z",
                               shared=False,
                               body=taxcode_body))
        res = yield http_client.fetch(base_url + "/api/taxcodes",
                                     method="POST",
                                     body=body)
        
        assert res.code == 200
        
        db_session = app.db_session()
        
        data = json.loads(res.body.decode("utf8"))
        assert "created_at" in data["taxcode"]
        assert "updated_at" in data["taxcode"]
        
        taxcode = db_session.query(Taxcode).get(data["taxcode"]["id"])
        assert taxcode.title == "Test Taxcode"
        