cont = "c"

#This while loop checks whether a given number is even or odd. I'm curious if it would be better to have the loop end when an invalid option is entered or if it should be treated like a c.
#Do we want it to only quit if q is entered or do we only want it to continue as long as c is entered?

while cont == "c":
    cont = input("Enter option ('c' to check, 'q' to quit): ")
    if cont == "q":
        print("Program terminated.")
        break
    elif cont == "c":
        num = int(input("Enter a number: "))
        if num % 2 == 0:
            print(f"The number {num} is even.")
        elif num % 2 == 1:
            print(f"The number {num} is odd.")
        else:
            print(f"The number entered is invalid.")
    else:
        print("Invalid input.")
    