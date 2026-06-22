population = int(input("Enter starting population: "))
gr = float(input("Enter hourly growth rate: "))
hours = int(input("Enter number of hours: "))

population_history = []
x = range(hours + 1)

for n in x:
    population_history.append(population)
    population *= gr

# Originally I was having an issue getting hour 0 and the original population to print. I just reversed the order of the iteration and adding the new number to the list and that solved the issue.

hour = 0

for i in population_history:
    print(f"Hour {hour}: {i:.2f}")
    hour += 1