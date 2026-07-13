import pytest
from dessert import *

@pytest.fixture
def dessert():
    return DessertItem()

@pytest.fixture
def candy():
    return Candy()

@pytest.fixture
def cookie():
    return Cookie()

@pytest.fixture
def iceCream():
    return IceCream()

@pytest.fixture
def sundae():
    return Sundae()

class Test_DessertItem:
    def test_dessert_default_value(self, dessert):
        assert dessert.name == ""

    def test_desset_passed_value(self):
        dessert = DessertItem("Kollin")
        assert dessert.name == "Kollin"
    
    def test_dessert_updated_value(self, dessert):
        dessert.name = "Kollin"
        assert dessert.name == "Kollin"

class Test_Candy:
    def test_candy_default_values(self, candy):
        assert candy.name == ""
        assert candy.candy_weight == 0.0
        assert candy.price_per_pound == 0.0

    def test_candy_passed_values(self):
        candy = Candy("Snickers", 2.5, 0.5)
        assert candy.name == "Snickers"
        assert candy.candy_weight == 2.5
        assert candy.price_per_pound == 0.5

    def test_candy_updated_values(self, candy):
        candy.name = "Snickers"
        candy.candy_weight = 2.5
        candy.price_per_pound = 0.5

        assert candy.name == "Snickers"
        assert candy.candy_weight == 2.5
        assert candy.price_per_pound == 0.5

class Test_Cookie:
    def test_cookie_default_values(self,cookie):
        assert cookie.name == ""
        assert cookie.cookie_quantity == 0
        assert cookie.price_per_dozen == 0.0

    def test_cookie_passed_values(self):
        cookie = Cookie("CC", 12, 5.0)

        assert cookie.name == "CC"
        assert cookie.cookie_quantity == 12
        assert cookie.price_per_dozen == 5.0

    def test_cookie_updated_values(self, cookie):
        cookie.name = "CC"
        cookie.cookie_quantity = 12
        cookie.price_per_dozen = 5.0

        assert cookie.name == "CC"
        assert cookie.cookie_quantity == 12
        assert cookie.price_per_dozen == 5.0

class Test_IceCream:
    def test_iceCream_default_values(self, iceCream):
        assert iceCream.name == ""
        assert iceCream.scoop_count == 0
        assert iceCream.price_per_scoop == 0.0

    def test_iceCream_passed_values(self):
        iceCream = IceCream("Chocolate", 3, 1.0)

        assert iceCream.name == "Chocolate"
        assert iceCream.scoop_count == 3
        assert iceCream.price_per_scoop == 1.0

    def test_iceCream_updated_values(self, iceCream):
        iceCream.name = "Chocolate"
        iceCream.scoop_count = 3
        iceCream.price_per_scoop = 1.0

        assert iceCream.name == "Chocolate"
        assert iceCream.scoop_count == 3
        assert iceCream.price_per_scoop == 1.0

class Test_Sundae:
    def test_sundae_default_values(self, sundae):
        assert sundae.name == ""
        assert sundae.scoop_count == 0
        assert sundae.price_per_scoop == 0.0
        assert sundae.topping_name == ""
        assert sundae.topping_price == 0.0

    def test_sundae_passed_values(self):
        sundae = Sundae("Chocolate", 3, 1.0, "PB", 1.0)

        assert sundae.name == "Chocolate"
        assert sundae.scoop_count == 3
        assert sundae.price_per_scoop == 1.0
        assert sundae.topping_name == "PB"
        assert sundae.topping_price == 1.0

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
