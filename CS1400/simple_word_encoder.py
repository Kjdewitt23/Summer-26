from string import ascii_lowercase

lower = ascii_lowercase

# The shift works because the remaineder of a lower number divided by a higher number is just the lower number. So, having the %26 in the shift allows the index to wrap around back to a.

def shift_letter(char, shift):
    shifted_char = lower[(lower.index(char) + shift) % 26]
    return shifted_char

def encode_word(word, shift):
    enc_word = ""
    for char in word:
       enc_word += shift_letter(char, shift)
    print(f"Encoded word: {enc_word}")
    return enc_word

word = input("Enter a word to encode: ")
shift = int(input("Enter a positive shift value: "))

# I forced lowercase by letting the user input any word then converting it to lower in the function call.

encode_word(word.lower(), shift)