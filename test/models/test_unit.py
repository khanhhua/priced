from app.models import Scenario

def test_instantiation():
    content = \
"""
[products]
P001 Banana 1kg
P002 Lemon 2kg
P003 Orange 5kg

[services]
S001 Shipping

[dates]
order = 2017-01-01T00:00:00Z
"""
    scenario = Scenario(id="ID001",
                        title="Simple Scenario",
                        description="Simple Description",
                        content=content)
    
    assert scenario.id == "ID001"
    assert scenario.title == "Simple Scenario"
    assert scenario.description == "Simple Description"
    assert scenario.content == content


def test_serialization():
    content = \
"""
[products]
P001 Banana 1kg
P002 Lemon 2kg
P003 Orange 5kg

[services]
S001 Shipping

[dates]
order = 2017-01-01T00:00:00Z
"""
    scenario = Scenario(id="ID001",
                        title="Simple Scenario",
                        description="Simple Description",
                        content=content)
    
    dict_data = scenario.to_dict()
    
    assert dict_data["id"] == "ID001"
    assert dict_data["title"] == "Simple Scenario"
    assert dict_data["description"] == "Simple Description"