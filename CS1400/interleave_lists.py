def interleave(odds, evens):
    interleaved_list = []
    # When I didn't have the 'min' method in there I got an index error because the lists aren't the same length.
    for i in range(min(len(odds), len(evens))):
        interleaved_list.append(odds[i])
        interleaved_list.append(evens[i])
    # These two extends add whatever part of the lists is longer than the length of the other list. Not having the second argument after the : makes it go to the end of the list. 
    interleaved_list.extend(odds[len(evens):])
    interleaved_list.extend(evens[len(odds):])
    return interleaved_list

def main():
    odds = [11,33,55]
    evens = [22,44,66,88]
    result = interleave(odds, evens)
    print(f"Interleaved list: {result}")

if __name__ == "__main__":
    main()