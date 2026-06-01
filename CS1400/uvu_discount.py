price = float(input("Enter the item price: "))
bt = input("Enter buyer type ('s' for student, 'f' for faculty): ")

if bt == "s":
    final_price = price - (price * 0.05)
    print(f"Final price after 5% discount: ${final_price:.2f}")
elif bt == "f":
    final_price = price - (price * 0.08)
    print(f"Final price after 8% discount: ${final_price:.2f}")
else:
    print("Incorrect buyer type entered. Please enter either 's' or 'f'.")

# Just thinking of how to turn this into a function that could be used for discounts in general and not just as a simple script.
# I'd make price and discount percentage the 2 parameters for it. I think that could be useful for a store in general.