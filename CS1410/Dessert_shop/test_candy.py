import pytest
from dessert import Candy

@pytest.fixture
def candy():
    return Candy()

@pytest.fixture
def candy_vals():
    return Candy("Snickers", 2.5, 0.5)


class Test_Candy:
    def test_candy_default_values(self, candy):
        assert candy.name == ""
        assert candy.candy_weight == 0.0
        assert candy.price_per_pound == 0.0

    def test_candy_passed_values(self, candy_vals):
        assert candy_vals.name == "Snickers"
        assert candy_vals.candy_weight == 2.5
        assert candy_vals.price_per_pound == 0.5

    def test_candy_updated_values(self, candy):
        candy.name = "Snickers"
        candy.candy_weight = 2.5
        candy.price_per_pound = 0.5

        assert candy.name == "Snickers"
        assert candy.candy_weight == 2.5
        assert candy.price_per_pound == 0.5

    def test_candy_calculate_cost_method(self, candy_vals):
        assert candy_vals.calculate_cost() == 1.25 

    def test_candy_calculate_tax_super_method(self, candy_vals):
        assert candy_vals.calculate_tax() == 0.09

    def test_candy_packaging(self, candy):
        assert candy.packaging == "Bag"