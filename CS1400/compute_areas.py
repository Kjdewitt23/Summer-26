import math

#Circle -- Formula == pi * r **2

radius = float(input("Enter the radius: "))
result = round(math.pi * radius ** 2, 4)
print(f"The area of the circle with radius {radius} is {result}")

#Rectangle -- Formula == width * height

width = float(input("Enter the width: "))
height = float(input("Enter the height: "))
result = round(width * height, 4)
print(f"The area of the rectangle with width {width} and height {height} is {result}")

#Triangle -- Formula == base * height / 2

base = float(input("Enter the base: "))
height = float(input("Enter the height: "))
result = round(base * height / 2, 4)
print(f"The area of the triangle with base {base} and height {height} is {result}")

#I chose to convert all the inputs to floats instead of ints because it led to errors when the user input a float. There is a way to restrict input but I didn't think it necessary for this project. 