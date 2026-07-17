import sys
from pathlib import Path

def main():

    book = Path(sys.argv[1])

    lst = []
    avg = 0
    bookCode = book.stem #I'm not sure if there is a different way to do this but this library made it simple to remove the extension from a path. 

    with open(book, "r", encoding = "utf-8") as f, open(f"{bookCode}_book.txt", "w") as nb:
        for line in f:
            stp = line.strip()
            tup = tuple(stp.split('|'))
            lst.append(tup)

        lst.sort(key=lambda item: int(item[1]))

        lenSort = sorted(lst, key=lambda l: -len(l[0]))
        longLine = lenSort[0][0]

        for item in lenSort:
            avg += len(item[0])
        average = round(avg / len(lenSort))

        nb.write(f"{bookCode}\n")
        nb.write(f"Longest line({lenSort[0][1]}): {longLine}\n")
        nb.write(f"Average length: {average}\n")

        for item in lst:
            nb.write(f"{item[0]}\n")


if __name__ == "__main__":
    main()