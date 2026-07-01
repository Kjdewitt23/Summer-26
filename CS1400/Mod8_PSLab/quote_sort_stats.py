ql = []

def averageLen(lst):
    '''Finds the average length of first elements in a list of tuples'''
    avg = 0
    for i in range(len(lst)):
        avg += len(lst[i][0])
    average = round(avg / len(lst))
    return average

with open("quotes_data-1.txt", "r") as file1:
    for line in file1:
        newTup = tuple(line.split("|"))
        ql.append(newTup)

ql = sorted(ql, key =lambda q: (-len(q[0]), q))

totalQuotes = len(ql)
avgLen = averageLen(ql)

lenSort = sorted(ql, key=lambda q: -len(q[0].split()))
longQuote = lenSort[0][0]

print(f"Total quotes: {totalQuotes}")
print(f"Average quote length: {avgLen}")
print(f"Quote with most words: {longQuote}")

with open("sorted_quotes.txt", "w") as output:
    output.write("Sorted Quotes\n")
    output.write("============================================\n")
    for i in range(len(ql)):
        output.write(f"{ql[i][0]} | {ql[i][1]} \n")
    output.write("Statistics\n")
    output.write("============================================\n")
    output.write(f"Total quotes: {totalQuotes}\n")
    output.write(f"Average quote length: {avgLen}\n")
    output.write(f"Quote with most words: {longQuote}\n")