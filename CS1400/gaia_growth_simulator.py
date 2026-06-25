import sys
# Growth function. I have the first write so that we always get the initial population in the file.
def logEq(initPop, rate, steps, fileName):
    population = [initPop]
    with open(fileName, "w") as f:
        f.write(f"0\t {population[0]:.3f}\n")
        for n in range(1, steps +1):
            p_n = rate * population[-1] * (1 - population[-1])
            population.append(p_n)
            f.write(f"{n}\t {population[n]:.3f}\n")

def main():
    # Using the different try except blocks, I can validate input type for the floats and ints. The if statements after them validate the range.
    try:
        population = float(sys.argv[1])
    except ValueError:
        print("Error: Population must be a number")
        sys.exit(1)
    if not (0 < population < 1):
        print("Error: Population must be between 0 and 1.")
        sys.exit(1)

    try:
        rate = float(sys.argv[2])
    except ValueError:
        print("Error: Rate must be a number")
        sys.exit(1)
    if not (0 < rate < 4):
        print("Error: Rate must be between 0 and 4.")
        sys.exit(1)

    try:
        steps = int(sys.argv[3])
    except ValueError:
        print("Error: Steps must be a number")
        sys.exit(1)
    if not (0 < steps):
        print("Error: Steps must be a positive number.")
        sys.exit(1)

    fileName = sys.argv[4]
    if not "." in fileName:
        print("FileName must have an extension.")
        sys.exit(1)

    logEq(population,rate,steps,fileName)

if __name__ == "__main__":
    main()