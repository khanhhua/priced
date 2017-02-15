import pytest
import json

from app.models import Base, Scenario

class TestScenariosApi(object):
    
    @pytest.mark.gen_test(run_sync=False)
    def test_list(self, http_client, base_url, app):
        res = yield http_client.fetch(base_url + "/api/scenarios")
        
        assert res.code == 200
        data = json.loads(res.body.decode("utf8"))
        
        assert len(data["scenarios"]) >= 0
        
    @pytest.mark.gen_test(run_sync=False)
    def test_create(self, http_client, base_url, app):
        content = \
"""
[products]
- P001 Banana 1kg
- P002 Banana 1kg

[services]
- shipping

[dates]
- order: 2017-01-31T00:00:00Z
"""
        body = json.dumps(dict(title="Simple",
                              description="Simple Dek",
                              content=content))
        res = yield http_client.fetch(base_url + "/api/scenarios",
                                     method="POST",
                                     body=body)
        
        assert res.code == 200
        
        db_session = app.db_session()
        
        data = json.loads(res.body.decode("utf8"))
        scenario = db_session.query(Scenario).get(data['scenario']['id'])
        assert scenario.title == "Simple"
        