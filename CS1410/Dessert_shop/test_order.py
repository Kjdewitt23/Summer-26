import pytest
from dessert import *

@pytest.fixture
def order():
    return Order()

@pytest.fixture
def order_vals():
    order = Order()
    order.add(Candy("Snickers", 2.5, 0.5))
    order.add(Cookie("CC", 12, 5.0))
    order.add(IceCream("Chocolate", 3, 1.0))
    order.add(Sundae("Chocolate", 3, 1.0, "PB", 1.0))
    order.pay_type = "CARD"
    return order

class Test_Order:
    def test_order_defualt_values(self, order):
        assert order.order == []
        assert order.pay_type == "CASH"

    def test_order_get_pay_type(self, order_vals):
        assert order_vals.get_pay_type() == "CARD"

    def test_order_set_pay_type(self, order_vals):
        order_vals.set_pay_type("PHONE")
        assert order_vals.pay_type == "PHONE" 

    def test_order_pay_type_error(self, order_vals):
        with pytest.raises(ValueError):
            order_vals.set_pay_type("Money")