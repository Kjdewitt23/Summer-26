from abc import ABC, abstractmethod
from packaging import Packaging
from payment import Payable, PayType

class DessertItem(ABC, Packaging):
    def __init__(self, name:str = "", tax_percent:float = 7.25):
        self.name = name
        self.tax_percent = tax_percent
        self._packaging = None

    @abstractmethod
    def calculate_cost(self) -> float:
        pass

    @property
    def packaging(self):
        return self._packaging

    @packaging.setter
    def packaging(self, value):
        self._packaging = value

    def calculate_tax(self):
        tax = self.calculate_cost() * (self.tax_percent / 100)
        return round(tax, 2)

    def __eq__(self, other):
        if not isinstance(other, DessertItem):
            return NotImplemented

        return self.calculate_cost() == other.calculate_cost()

    def __ne__(self, other):
        if not isinstance(other, DessertItem):
            return NotImplemented

        return self.calculate_cost() != other.calculate_cost()

    def __lt__(self, other):
        if not isinstance(other, DessertItem):
            return NotImplemented

        return self.calculate_cost() < other.calculate_cost()

    def __gt__(self, other):
        if not isinstance(other, DessertItem):
            return NotImplemented

        return self.calculate_cost() > other.calculate_cost()

    def __le__(self, other):
        if not isinstance(other, DessertItem):
            return NotImplemented

        return self.calculate_cost() <= other.calculate_cost()

    def __ge__(self, other):
        if not isinstance(other, DessertItem):
            return NotImplemented

        return self.calculate_cost() >= other.calculate_cost()
    

class Candy(DessertItem):
    def __init__(self, name:str = "", candy_weight:float = 0.0, price_per_pound:float = 0.0):
        super().__init__(name)
        self.packaging = "Bag"
        self.candy_weight = candy_weight
        self.price_per_pound = price_per_pound

    def __str__(self):
        return f"{self.name} ({self.packaging})\n -    {self.candy_weight} lbs. @ ${self.price_per_pound}/lb:, ${self.calculate_cost()}, [Tax: ${self.calculate_tax()}]"

    def calculate_cost(self):
        cost = self.candy_weight * self.price_per_pound
        return round(cost, 2)

class Cookie(DessertItem):
    def __init__(self, name:str = "", cookie_quantity:int = 0, price_per_dozen:float = 0.0):
        super().__init__(name)
        self.packaging = "Box"
        self.cookie_quantity = cookie_quantity
        self.price_per_dozen = price_per_dozen

    def __str__(self):
        return f"{self.name} Cookies ({self.packaging})\n -    {self.cookie_quantity} cookies. @ ${self.price_per_dozen}/dozen:, ${self.calculate_cost()}, [Tax: ${self.calculate_tax()}]"

    def calculate_cost(self):
        cost = (self.cookie_quantity / 12) * self.price_per_dozen
        return round(cost, 2)
    
class IceCream(DessertItem):
    def __init__(self, name:str = "", scoop_count:int = 0, price_per_scoop:float = 0.0):
        super().__init__(name)
        self.packaging = "Bowl"
        self.scoop_count = scoop_count
        self.price_per_scoop = price_per_scoop

    def __str__(self):
        return f"{self.name} Ice Cream ({self.packaging})\n-    {self.scoop_count} scoops. @ ${self.price_per_scoop}/scoop:, ${self.calculate_cost()}, [Tax: ${self.calculate_tax()}]"

    def calculate_cost(self):
        cost = self.scoop_count * self.price_per_scoop
        return round(cost, 2)

class Sundae(IceCream):
    def __init__(self, name:str = "", scoop_count:int = 0, price_per_scoop:float = 0.0, topping_name:str = "", topping_price:float = 0.0):
        super().__init__(name, scoop_count, price_per_scoop)
        self.packaging = "Boat"
        self.topping_name = topping_name
        self.topping_price = topping_price

    def __str__(self):
        return f"{self.topping_name} {self.name} Sundae ({self.packaging})\n -    {self.scoop_count} scoops. @ ${self.price_per_scoop}/scoop\n-    {self.topping_name} @ ${self.topping_price}:, ${self.calculate_cost()}, [Tax: ${self.calculate_tax()}]"

    def calculate_cost(self):
        cost = (self.scoop_count * self.price_per_scoop) + self.topping_price
        return round(cost, 2)

class Order(Payable):
    def __init__(self):
        self.order = []
        self.pay_type = "CASH"

    def get_pay_type(self):
        return self.pay_type

    def set_pay_type(self, payment_method: PayType):
        if payment_method not in ("CASH", "CARD", "PHONE"):
            raise ValueError("Please enter a valid payment type.")

        self.pay_type = payment_method

    def __str__(self):
        items = "\n".join(str(item) for item in self.order)
        return f"{items}\nPaid with {self.get_pay_type()}"
    
    def to_list(self):
        lines = str(self).split("\n")
        return [line.split(",") for line in lines]
    
    def add(self, item):
        self.order.append(item)

    def __len__(self):
        return len(self.order)
    
    def __iter__(self):
        return iter(self.order)
    
    def order_cost(self):
        total = 0
        for item in self.order:
            total += item.calculate_cost()
        return round(total, 2)
    
    def order_tax(self):
        total_tax = 0
        for item in self.order:
            total_tax += item.calculate_cost() * (item.tax_percent / 100)
        return round(total_tax, 2)

    def sort(self):
        s_lst = sorted(self.order)
        return s_lst