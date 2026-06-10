def encode(mess, sv):
    result = ""
    for char in mess:
        if char.isupper():
            result += chr((ord(char) - 65 + sv) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 + sv) % 26 + 97)
        else:
            result += char
    return result

# I feel like this would be cleaner to write 1 function that takes a 3rd parameter asking for encode or decode then it just makes the shift value positive or negative based on that value. The instructions say to have 2 separate functions though.

def decode(mess, sv):
    result = ""
    sv = -sv
    for char in mess:
        if char.isupper():
            result += chr((ord(char) - 65 + sv) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 + sv) % 26 + 97)
        else:
            result += char
    return result

def main():
    eod = ""
    while eod == 'e' or 'd':
        message = input("Enter a message: ")
        sv = int(input("Enter shift value: "))
        eod = input("Choose (e)ncode or (d)ecode: ")
        if eod == "e":
            result = encode(message, sv)
            print(f"Encoded message: {result}")
            break
        elif eod == "d":
            result = decode(message, sv)
            print(f"Decoded message: {result}")
            break
        else:
            print("Please enter 'e' to encode or 'd' to decode.")

if __name__ == '__main__':
    main()