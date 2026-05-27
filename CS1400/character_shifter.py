from string import ascii_lowercase, ascii_uppercase

char = input("Enter a character: ")
sv = int(input("Enter shift value: "))
dir = input("Enter direction (forward/backward): ")
lower = ascii_lowercase
upper = ascii_uppercase

def shift_character(char, shift, mode):
    if char.isalpha() == False:
        return char
    elif mode == "forward":
        if char in lower:
            shifted_char = lower[(lower.index(char) + shift) % 26]
        else:
            shifted_char = upper[(upper.index(char) + shift) % 26]
        return shifted_char
    else:
        if char in lower:
            shifted_char = lower[(lower.index(char) - shift) % 26]
        else:
            shifted_char = upper[(upper.index(char) - shift) % 26]
    return shifted_char
    
    
result = shift_character(char, sv, dir)
print(f"Shifted character: {result}")

# I originally had the function like this but realized after testing that nothing was making the character maintain casing. 
# def shift_character(char, shift, mode):
#     if char.isalpha() == False:
#         return char
#     elif mode == "forward":
#         shifted_char = ord(char) + shift
#         shifted_char = chr(shifted_char)
#         return shifted_char
#     else:
#         shifted_char = ord(char) - shift
#         shifted_char = chr(shifted_char)
#         return shifted_char