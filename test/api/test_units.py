import pytest
import json

from app.models import Base, Unit

class TestUnitsApi(object):
    
    @pytest.mark.gen_test(run_sync=False)
    def test_list(self, http_client, base_url, app):
        res = yield http_client.fetch(base_url + "/api/units")
        
        assert res.code == 200
        data = json.loads(res.body.decode("utf8"))
        
        assert len(data["units"]) >= 0
        
    @pytest.mark.gen_test(run_sync=False)
    def test_create(self, http_client, base_url, app):
        body = json.dumps(dict(name="Kilogram",
                              short_form="kg"))
        res = yield http_client.fetch(base_url + "/api/units",
                                     method="POST",
                                     body=body)
        
        assert res.code == 200
        
        db_session = app.db_session()
        
        data = json.loads(res.body.decode("utf8"))
        unit = db_session.query(Unit).get(data['unit']['id'])
        assert unit.name == "Kilogram"
        