scorebook = {}
scorebook["Alice"] = 88
scorebook["Bob"] = 75
scorebook["Charlie"] = 93
scorebook["Dana"] = 80

for item in scorebook.items():
    '''Loops through items in the score book and prints them so they are better formatted'''
    print(f"{item[0]}: {item[1]}")

scorebook["Dana"] = 85
'''UPdates Dana's score'''
print(f"Updated Dana's score to {scorebook["Dana"]}")

scorebook.pop("Bob")
'''Removes Bob from the scorebook'''
print("Removed Bob from the scorebook")

x = scorebook.get("Eve", "Eve is not found in the scorebook")
'''Searches for Eve in scorebook and returns a message when that key isn't found'''
print(x)

total = 0
for score in scorebook.values():
    total += score

av = total / len(scorebook)
print(f"Average score: {av:.2f}")

