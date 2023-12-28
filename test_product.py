import pytest
from products import Product


def test_create_normal_product():
    # Test that creating a normal product works
    product = Product("Laptop", price=1200, quantity=50)
    assert product.name == "Laptop"
    assert product.price == 1200
    assert product.quantity == 50
    assert product.is_active()  # By default, the product should be active


def test_create_empty_name_product():
    # Test that creating a product with an empty name invokes an exception
    with pytest.raises(ValueError, match="Invalid input: name cannot be empty"):
        Product("", price=1200, quantity=50)


def test_create_negative_price_product():
    # Test that creating a product with a negative price invokes an exception
    with pytest.raises(ValueError, match="Invalid input: .* price/quantity must be non-negative."):
        Product("MacBook Air M2", price=-10, quantity=100)


def test_create_negative_quantity_product():
    # Test that creating a product with a negative quantity invokes an exception
    with pytest.raises(ValueError, match="Invalid input: .* price/quantity must be non-negative."):
        Product("Laptop", price=1200, quantity=-100)


def test_product_becomes_inactive_at_zero_quantity():
    # Test that when a product reaches 0 quantity, it becomes inactive
    product = Product("Laptop", price=1200, quantity=1)
    product.buy(1)  # Reduce quantity to 0
    assert not product.is_active()


def test_product_purchase_modifies_quantity_and_returns_output():
    # Test that product purchase modifies the quantity and returns the right output
    product = Product("Tablet", price=500, quantity=10)
    total_cost = product.buy(3)
    assert product.quantity == 7  # Quantity should be reduced by 3
    assert total_cost == 1500  # Total cost = quantity * price


def test_buying_larger_quantity_than_exists_invokes_exception():
    # Test that buying a larger quantity than exists invokes an exception
    product = Product("Smartphone", price=800, quantity=5)
    with pytest.raises(ValueError, match="Invalid quantity for purchase."):
        product.buy(7)  # Attempt to buy more than available quantity


def test_set_quantity():
    # Test the set_quantity method to ensure it modifies the quantity correctly
    product = Product("Mouse", price=20, quantity=15)
    product.set_quantity(10)
    assert product.quantity == 10


def test_set_quantity_with_negative_value():
    # Test that setting quantity to a negative value raises an exception
    product = Product("Keyboard", price=30, quantity=25)
    with pytest.raises(ValueError, match="Quantity must be non-negative."):
        product.set_quantity(-5)


def test_activate_and_deactivate():
    # Test activate and deactivate methods
    product = Product("Monitor", price=200, quantity=8)
    product.deactivate()
    assert not product.is_active()
    product.activate()
    assert product.is_active()


pytest.main()
