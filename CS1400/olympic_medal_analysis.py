olympic_data = [
    ("USA", (15, 10, 8)),
    ("Australia", (10, 12, 4)),
    ("Japan", (6, 8, 10)),
    ("Argentina", (2, 3, 5)),
    ("UK", (8, 8, 7))
]

def medals(g):
    '''helper function for key of sort'''
    return g[1]

def analyze_medals(data):
    '''Takes a list of tuples, compares the values, sums them, and returns a list of tuples sorted by most medals won'''
    new_list = []
    most_gold = data[0][1][0]
    most_gold_country = data[0][0]

    for item in data:
        if item[1][0] > most_gold:
            most_gold = item[1][0]
            most_gold_country = item[0]
        
        new_tup = (item[0], sum(item[1]))
        new_list.append(new_tup)

    new_list.sort(reverse=True, key=medals)
    return new_list, most_gold_country
    
def main():
    results, winner = analyze_medals(olympic_data)

    print(f"Total Medal Counts:")
    
    ind = 1

    for i in results:
        print(f"{ind}. {i[0]} - {i[1]} medals")
        ind += 1
    print(f"Country with the most gold medals: {winner}")

if __name__ == "__main__":
    main()