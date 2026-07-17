from dessert import *
from tabulate import tabulate

def main():
    new_order = Order()

    new_order.add(Candy("Candy Corn", 1.5, .25))
    new_order.add(Candy("Gummy Bears", .25, .35))
    new_order.add(Cookie("Chocolate Chip", 6, 3.99))
    new_order.add(IceCream("Pistachio", 2, .79))
    new_order.add(Sundae("Vanilla", 3, .69, "Hot Fudge", 1.29))
    new_order.add(Cookie("Oatmeal Raisin", 2, 3.45))
    
    data = []
    subtotal = 0
    tax = 0

    for item in new_order:
        cost = item.calculate_cost()
        item_tax = item.calculate_tax()

        subtotal += cost
        tax += item_tax

        data.append([
            item.name,
            f"${cost:.2f}",
            f"${item_tax:.2f}"
        ])
    total = subtotal + tax

    data.append(["Order Subtotal", f"${subtotal:.2f}", f"${tax:.2f}"])
    data.append(["Order Total", "", f"${total:.2f}"])

    print(tabulate(data, headers=["Name", "Cost", "Tax"], tablefmt="fancy_grid"))

    print(f"Total number of items in order: {len(new_order)}")

if __name__ == "__main__":
    main()