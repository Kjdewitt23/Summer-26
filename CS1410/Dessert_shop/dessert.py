from abc import ABC, abstractmethod

class DessertItem(ABC):
    def __init__(self, name:str = "", tax_percent:float = 7.25):
        self.name = name
        self.tax_percent = tax_percent

    @abstractmethod
    def calculate_cost(self) -> float:
        pass

    def calculate_tax(self):
        tax = self.calculate_cost() * (self.tax_percent / 100)
        return round(tax, 2)


class Candy(DessertItem):
    def __init__(self, name:str = "", candy_weight:float = 0.0, price_per_pound:float = 0.0):
        super().__init__(name)
        self.candy_weight = candy_weight
        self.price_per_pound = price_per_pound

    def calculate_cost(self):
        cost = self.candy_weight * self.price_per_pound
        return round(cost, 2)

class Cookie(DessertItem):
    def __init__(self, name:str = "", cookie_quantity:int = 0, price_per_dozen:float = 0.0):
        super().__init__(name)
        self.cookie_quantity = cookie_quantity
        self.price_per_dozen = price_per_dozen

    def calculate_cost(self):
        cost = (self.cookie_quantity / 12) * self.price_per_dozen
        return round(cost, 2)
    
class IceCream(DessertItem):
    def __init__(self, name:str = "", scoop_count:int = 0, price_per_scoop:float = 0.0):
        super().__init__(name)
        self.scoop_count = scoop_count
        self.price_per_scoop = price_per_scoop

    def calculate_cost(self):
        cost = self.scoop_count * self.price_per_scoop
        return round(cost, 2)

class Sundae(IceCream):
    def __init__(self, name:str = "", scoop_count:int = 0, price_per_scoop:float = 0.0, topping_name:str = "", topping_price:float = 0.0):
        super().__init__(name, scoop_count, price_per_scoop)
        self.topping_name = topping_name
        self.topping_price = topping_price

    def calculate_cost(self):
        cost = (self.scoop_count * self.price_per_scoop) + self.topping_price
        return round(cost, 2)

class Order():
    def __init__(self):
        self.order = []
    
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