def word_count(text):
    '''Takes a given paragraph and counts the number of each word and how many times it occurs'''
    new_text = text.split()
    word_counter = {}
    for word in new_text:
        if word in word_counter:
            word_counter[word] += 1
        if word not in word_counter:
            word_counter[word] = 1
        
    return word_counter

def main():
    sample_text = "This is a sample paragraph It has a few words that repeat such as a is few and sample"

    counted_words = word_count(sample_text)

    more_words = counted_words.copy()

    for word, count in list(more_words.items()): #I was having a hard time checking the value while trying to iterate just over more_words.items() so I turned it into a list of lists and made that work. I was also thinking of a dictionary comprehension but I wasn't sure how to copy the original dict while also doing that.
        if count == 1:
            more_words.pop(word)

    print("Original Word Frequencies:")

    for word in counted_words.items():
        print(f"{word[0]}: {word[1]}")

    print("\nAfter removing words with only one occurence:")

    for word in more_words.items():
        print(f"{word[0]}: {word[1]}")

if __name__ == "__main__":
    main()