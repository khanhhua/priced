from app.models import Product

def test_product_instantiation():
    product = Product(id="ID001", name="Test Product", kind="generic")
    
    assert product.id == "ID001"
    assert product.name == "Test Product"
    assert product.kind == "generic"
    
def test_product_serialization():
    product = Product(id="ID001", name="Test Product", kind="generic")
    
    dict_data = product.to_dict()
    
    assert dict_data["id"] == "ID001"
    assert dict_data["name"] == "Test Product"
    assert dict_data["kind"] == "generic"