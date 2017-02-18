from datetime import datetime
from app.models import Taxcode

def test_instantiation():
    body = \
"""
TAX 10% "Tax 10% based on price"
"""
    taxcode = Taxcode(id="ID001",
                      title="Test Taxcode",
                      effective_at=datetime(2017, 1, 1, 0, 0, 0),
                      expired_at=datetime(2017, 2, 28, 0, 0, 0),
                      shared=False,
                      body=body)
    
    assert taxcode.id == "ID001"
    assert taxcode.title == "Test Taxcode"
    assert taxcode.effective_at == datetime(2017, 1, 1, 0, 0, 0)
    assert taxcode.expired_at == datetime(2017, 2, 28, 0, 0, 0)
    assert taxcode.shared == False
    assert taxcode.body == body
    
def test_serialization():
    body = \
"""
TAX 10% "Tax 10% based on price"
"""
    taxcode = Taxcode(id="ID001",
                      title="Test Taxcode",
                      effective_at=datetime(2017, 1, 1, 0, 0, 0),
                      expired_at=datetime(2017, 2, 28, 0, 0, 0),
                      shared=False,
                      body=body)
    dict_data = taxcode.to_dict()
    
    assert dict_data["id"] == "ID001"
    assert dict_data["title"] == "Test Taxcode"
    assert dict_data["effective_at"] == "2017-01-01T00:00:00"
    assert dict_data["expired_at"] == "2017-02-28T00:00:00"
    assert dict_data["shared"] == False
    assert dict_data["body"] == body