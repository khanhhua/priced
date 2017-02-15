from app.models import Scenario

def test_instantiation():
    content = \
"""
[products]
P001 Banana 1kg
P002 Orange 2kg
P004 Lemon 4kg

[services]
Shipping

[dates]
"""
    scenario = Scenario(id="ID001",
                        title="Simple Scenario",
                        description="Simple Description",
                        content=content)
    
    assert scenario.id == "ID001"
    assert scenario.title == "Simple Scenario"
    assert scenario.description == "Simple Description"


def test_serialization():
    content = \
"""
[products]
P001 Banana 1kg
P002 Orange 2kg
P004 Lemon 4kg

[services]
Shipping

[dates]
"""
    scenario = Scenario(id="ID001",
                        title="Simple Scenario",
                        description="Simple Description",
                        content=content)
    
    dict_data = scenario.to_dict()
    
    assert dict_data["id"] == "ID001"
    assert dict_data["title"] == "Simple Scenario"
    assert dict_data["description"] == "Simple Description"