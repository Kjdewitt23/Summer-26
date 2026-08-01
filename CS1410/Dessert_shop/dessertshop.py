from dessert import *
from tabulate import SEPARATING_LINE, tabulate

class DessertShop:
    def __init__(self):
        pass
    
    def get_float(self, prompt):
      while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Please enter a non-negative number.")
                continue
            return value
        except ValueError:
            print("Please enter a valid number.")
    
    def get_int(self, prompt):
      while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Please enter a non-negative integer.")
                continue
            return value
        except ValueError:
            print("Please enter a valid integer.")
   
    def user_prompt_candy(self):
        name = input("Enter name of candy: ")
        weight = self.get_float("Enter weight (lbs): ")
        price = self.get_float("Enter price per pound: ")
        return Candy(name, weight, price)

    def user_prompt_cookie(self):
        name = input("Enter type of cookie: ")
        quant = self.get_int("Enter number of cookies: ")
        price = self.get_float("Enter price per dozen: ")
        return Cookie(name, quant, price)

    def user_prompt_icecream(self):
        name = input("Enter the type of ice cream: ")
        scoops = self.get_int("Enter the number of scoops: ")
        price = self.get_float("Enter the price per scoop: ")
        return IceCream(name, scoops, price)

    def user_prompt_sundae(self):
        name = input("Enter the type of ice cream: ")
        scoops = self.get_int("Enter the number of scoops: ")
        price = self.get_float("Enter the price per scoop: ")
        topping = input("Enter the topping: ")
        tp = self.get_float("Enter the price for the topping: ")
        return Sundae(name, scoops, price, topping, tp)

    def user_prompt_payment(self):
      while True:
          try:
              payment = input("Enter payment type (CASH, CARD, PHONE): ").upper()
              return payment

          except ValueError:
              print("Please enter a valid payment type.")
    

def main():
    shop = DessertShop() 
    order = Order()
    
    # order.add(Candy('Candy Corn', 1.5, 0.25))
    # order.add(Candy('Gummy Bears', 0.25, 0.35))
    # order.add(Cookie('Chocolate Chip', 6, 3.99))
    # order.add(IceCream('Pistachio', 2, 0.79))
    # order.add(Sundae('Vanilla', 3, 0.69, 'Hot Fudge', 1.29))
    # order.add(Cookie('Oatmeal Raisin', 2, 3.45))
    
    done: bool = False
    # build the prompt string once
    prompt = '\n'.join([ '\n',
            '1: Candy',
            '2: Cookie',            
            '3: Ice Cream',
            '4: Sundae',
            '\nWhat would you like to add to the order? (1-4, Enter for done): '
      ])

    while not done:
      choice = input(prompt)
      match choice:
        case '':
          done = True
        case '1':            
          item = shop.user_prompt_candy()
          order.add(item)
          print(f'{item.name} has been added to your order.')
        case '2':            
          item = shop.user_prompt_cookie()
          order.add(item)
          print(f'{item.name} has been added to your order.')
        case '3':            
          item = shop.user_prompt_icecream()
          order.add(item)
          print(f'{item.name} has been added to your order.')
        case '4':            
          item = shop.user_prompt_sundae()
          order.add(item)
          print(f'{item.name} has been added to your order.')
        case _:            
          print('Invalid response:  Please enter a choice from the menu (1-4) or Enter')
    print()

    while True:
      try:
          payment = shop.user_prompt_payment()
          order.set_pay_type(payment)
          break
      except ValueError:
          print("Please enter a valid payment type.")

    order.order = order.sort()
    
    data = order.to_list()

    data.append(SEPARATING_LINE)

    data.append(["Order Subtotal", f"${order.order_cost():.2f}", f"${order.order_tax():.2f}"])
    data.append(["Order Total", "", f"${order.order_cost() + order.order_tax():.2f}"])
    data.append(["Total Items in the order:", "", len(order)])

    data.append(SEPARATING_LINE)

    data.append([f"Paid with {order.get_pay_type()}", "", ""])

    print(tabulate(data, headers=["Name", "Cost", "Tax"], tablefmt="psql"))

if __name__ == "__main__":
    main()