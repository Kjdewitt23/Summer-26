# I used while True loops to allow the user to re-enter values until they're valid. 
while True:
    name = input("Enter your name: ")
# I messed around with using name.isalpha() == false but I remembered you want to try to test positive statements if possible so I changed to the below line.
    if name.isnumeric():
        print("Invalid name. Please enter a non-numeric name.")
    else:
        break

while True:
    try:
        age = int(input("Enter your age: "))
        break
    except:
        print("Invalid age. Please enter an integer.")

print(f"Thanks, {name}! Your age is {age}.")
    
    