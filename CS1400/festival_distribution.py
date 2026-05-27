colonists = int(input("Enter the number of colonists: "))
foodSupply = int(input("Enter the total food units available: "))
rationsNeeded = colonists * 4
remainingSupply = foodSupply - rationsNeeded

#All the code prior to this comment is used from the first PS lab.

z_spec = remainingSupply * 0.15
#print(z_spec)
remainingSupply = remainingSupply - z_spec #Like was discussed in this week's lecture, I used 'remainingSupply' multiple times and just updated its value.
#print(remainingSupply)
l_spec = remainingSupply * 0.10
#print(l_spec)
remainingSupply = remainingSupply - l_spec
#print(remainingSupply)
colo_total = remainingSupply / colonists + 4 #I did the colonist total first because I can then simplify Zerin and Lyra's totals by adding their percentage to the colonist total.

z_total = z_spec + colo_total
l_total = l_spec + colo_total

print(f"Zerin's share: {z_total:.2f}")
print(f"Lyra's share: {l_total:.2f}")
print(f"Share per colonist: {colo_total:.2f}")

