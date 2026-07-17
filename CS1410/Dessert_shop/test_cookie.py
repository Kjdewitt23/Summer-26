import pytest
from dessert import Cookie

@pytest.fixture
def cookie():
    return Cookie()

@pytest.fixture
def cookie_vals():
    return Cookie("CC", 12, 5.0) 

class Test_Cookie:
    def test_cookie_default_values(self,cookie):
        assert cookie.name == ""
        assert cookie.cookie_quantity == 0
        assert cookie.price_per_dozen == 0.0

    def test_cookie_passed_values(self, cookie_vals):
        assert cookie_vals.name == "CC"
        assert cookie_vals.cookie_quantity == 12
        assert cookie_vals.price_per_dozen == 5.0

    def test_cookie_updated_values(self, cookie):
        cookie.name = "CC"
        cookie.cookie_quantity = 12
        cookie.price_per_dozen = 5.0

        assert cookie.name == "CC"
        assert cookie.cookie_quantity == 12
        assert cookie.price_per_dozen == 5.0

    def test_cookie_calculate_cost_method(self, cookie_vals):
        assert cookie_vals.calculate_cost() == 5

    def test_cookie_calculate_tax_super_method(self, cookie_vals):
        assert cookie_vals.calculate_tax() == 0.36