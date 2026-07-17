import pytest
from dessert import Sundae

@pytest.fixture
def sundae():
    return Sundae()

@pytest.fixture
def sundae_vals():
    return Sundae("Chocolate", 3, 1.0, "PB", 1.0)

class Test_Sundae:
    def test_sundae_default_values(self, sundae):
        assert sundae.name == ""
        assert sundae.scoop_count == 0
        assert sundae.price_per_scoop == 0.0
        assert sundae.topping_name == ""
        assert sundae.topping_price == 0.0

    def test_sundae_passed_values(self, sundae_vals):
        assert sundae_vals.name == "Chocolate"
        assert sundae_vals.scoop_count == 3
        assert sundae_vals.price_per_scoop == 1.0
        assert sundae_vals.topping_name == "PB"
        assert sundae_vals.topping_price == 1.0

    def test_sundae_updated_values(self, sundae):
        sundae.name = "Chocolate"
        sundae.scoop_count = 3
        sundae.price_per_scoop = 1.0
        sundae.topping_name = "PB"
        sundae.topping_price = 1.0

        assert sundae.name == "Chocolate"
        assert sundae.scoop_count == 3
        assert sundae.price_per_scoop == 1.0
        assert sundae.topping_name == "PB"
        assert sundae.topping_price == 1.0

    def test_sundae_calculate_cost_method(self, sundae_vals):
        assert sundae_vals.calculate_cost() == 4

    def test_sundae_calculate_tax_super_method(self, sundae_vals):
        assert sundae_vals.calculate_tax() == 0.29
