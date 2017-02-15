from app.models import Unit

def test_instantiation():
    unit = Unit(id="ID001", name="Kilogram", short_form="kg")
    
    assert unit.id == "ID001"
    assert unit.name == "Kilogram"
    assert unit.short_form == "kg"


def test_serialization():
    unit = Unit(id="ID001", name="Kilogram", short_form="kg")
    
    dict_data = unit.to_dict()
    
    assert dict_data["id"] == "ID001"
    assert dict_data["name"] == "Kilogram"
    assert dict_data["short_form"] == "kg"