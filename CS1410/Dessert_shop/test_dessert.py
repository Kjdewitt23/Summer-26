import pytest
from dessert import *

@pytest.fixture
def candy():
    return Candy()

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
        