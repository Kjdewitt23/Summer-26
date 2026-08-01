import pytest
from dessert import *

@pytest.fixture
def candy():
    return Candy()

@pytest.fixture
def candy_vals():
    return Candy("Snickers", 2.5, 0.5)

@pytest.fixture
def cookie_vals():
    return Cookie("CC", 12, 5.0) 

@pytest.fixture
def iceCream_vals():
    return IceCream("Chocolate", 2, 2.5)

class Test_DessertItem:
    def test_dessert_default_value(self, candy):
        assert candy.name == ""

    def test_desset_passed_value(self):
        dessert = Candy("Kollin")
        assert dessert.name == "Kollin"
    
    def test_dessert_updated_value(self, candy):
        candy.name = "Kollin"
        assert candy.name == "Kollin"

    def test_dessert_tax_percent_attr(self, candy):
        assert candy.tax_percent == 7.25

    def test_dessert_eq(self, cookie_vals, iceCream_vals):
        assert cookie_vals == iceCream_vals

    def test_dessert_ne(self, candy_vals, cookie_vals):
        assert candy_vals != cookie_vals

    def test_dessery_lt(self, candy_vals, iceCream_vals):
        assert candy_vals < iceCream_vals

    def test_dessery_gt(self, candy_vals, iceCream_vals):
        assert iceCream_vals > candy_vals

    def test_dessert_le(self, candy_vals, cookie_vals, iceCream_vals):
        assert candy_vals <= cookie_vals and cookie_vals <= iceCream_vals

    def test_dessert_ge(self, candy_vals, cookie_vals, iceCream_vals):
        assert cookie_vals >= candy_vals and cookie_vals >= iceCream_vals