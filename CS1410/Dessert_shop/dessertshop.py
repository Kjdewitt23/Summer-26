from dessert import *

def main():
    new_order = Order()

    new_order.add(Candy("Candy Corn", 1.5, .25))
    new_order.add(Candy("Gummy Bears", .25, .35))
    new_order.add(Cookie("Chocolate Chip", 6, 3.99))
    new_order.add(IceCream("Pistachio", 2, .79))
    new_order.add(Sundae("Vanilla", 3, .69, "Hot Fudge", 1.29))
    new_order.add(Cookie("Oatmeal Raisin", 2, 3.45))
    
    for item in new_order:
        print(item.name)

    print(f"Total number of items in order: {len(new_order)}")

if __name__ == "__main__":
    main()