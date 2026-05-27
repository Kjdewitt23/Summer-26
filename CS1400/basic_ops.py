num_1 = float(input("Enter the first number: "))
num_2 = float(input("Enter the second number: "))

# I feel like the example is misleading. it says to have the user enter an operation as well but that would lead to the use of conditionals that we haven't gone over yet.

def basic_math(first, second):
    add = first + second
    sub = first - second
    mult = first * second
    divide = first / second
    print(f"For inputs {first} and {second}: ")
    print(f"Addition: {add}")
    print(f"Subtraction: {sub:.2f}")
    print(f"Multiplication: {mult:.2f}")
    print(f"Division: {divide:.2f}")

# I was trying to do the printing outside of the function but we hadn't gon over tuples or how to return/work with them so I kep the print functions inside my function. 

basic_math(num_1, num_2)


