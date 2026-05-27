colonists = int(input("Enter the total number of colonists: "))
foodSupply = int(input("Enter the total amount of food units: "))
rationsNeeded = colonists * 4
remainingSupply = foodSupply - rationsNeeded

print("Original supply: " + str(foodSupply) + " units")
print("Ration allocation (4 units per colonist): " + str(rationsNeeded) + " units")
print("Festival stockpile remaining: " + str(remainingSupply) + " units")


