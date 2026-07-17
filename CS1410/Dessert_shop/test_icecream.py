import pytest
from dessert import IceCream

@pytest.fixture
def iceCream():
    return IceCream()

@pytest.fixture
def iceCream_vals():
    return IceCream("Chocolate", 3, 1.0)

class Test_IceCream:
    def test_iceCream_default_values(self, iceCream):
        assert iceCream.name == ""
        assert iceCream.scoop_count == 0
        assert iceCream.price_per_scoop == 0.0

    def test_iceCream_passed_values(self, iceCream_vals):
        assert iceCream_vals.name == "Chocolate"
        assert iceCream_vals.scoop_count == 3
        assert iceCream_vals.price_per_scoop == 1.0

    def test_iceCream_updated_values(self, iceCream):
        iceCream.name = "Chocolate"
        iceCream.scoop_count = 3
        iceCream.price_per_scoop = 1.0

        assert iceCream.name == "Chocolate"
        assert iceCream.scoop_count == 3
        assert iceCream.price_per_scoop == 1.0

    def test_iceCream_calculate_cost_method(self, iceCream_vals):
        assert iceCream_vals.calculate_cost() == 3

    def test_iceCream_calculate_tax_super_method(self, iceCream_vals):
        assert iceCream_vals.calculate_tax() == 0.22