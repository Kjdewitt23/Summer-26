import random
import string 

# Breaking this down into 3, incremental functions made the project a lot simpler. I was thinking of pushing it all into one function but that doesn't make sense. Helper functions work much better.

def make_word():
    length = random.randint(5,10)
    word = ""

    for i in range(length):
        word += random.choice(string.ascii_lowercase)
    return word

def make_line():
    num_words = random.randint(8,10)
    words = []

    for i in range(num_words):
        words.append(make_word())
    return " ".join(words)

def write_random_text():
    num_lines = random.randint(100,200)
    with open("randomText.txt", "w") as file:
        for i in range(num_lines):
            file.write(make_line() + "\n")

# Remembering about the random module took me a little bit. But, once I did, this was pretty simple. 

def main():
    write_random_text()

if __name__ == "__main__":
    main()