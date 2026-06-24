# I think this is the most memory effecient way to do this. It only reads a single line then iterates through the letters of each line. after that finishes, it reads the next line. That way it doesn't read the entire file every time.

def vowel_count(filePath):
    aNum = 0
    eNum = 0
    iNum = 0
    oNum = 0
    uNum = 0
    yNum = 0
    try:
        with open(filePath, "r") as f:
            for line in f:
                for char in line:
                    if char == "a":
                        aNum += 1
                    elif char == "e":
                        eNum += 1
                    elif char == "i":
                        iNum += 1
                    elif char == "o":
                        oNum += 1
                    elif char == "u":
                        uNum += 1
                    elif char == "y":
                        yNum += 1
                    else:
                        continue
    
    except FileNotFoundError as e:
        print(f"A file couldn't be found at the provided path. {e}")
    return aNum, eNum, iNum, oNum, uNum, yNum

def main():
    a,e,i,o,u,y = vowel_count("randomText.txt")

    print(f"There were {a} a's, {e} e's, {i} i's, {o} o's, {u} u's, and {y} y's.")

if __name__ == "__main__":
    main()