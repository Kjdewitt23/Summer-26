usr_str = input("Enter a string: ")
usr_char = input("Enter a character to count: ")

def char_count(string, character):
    count = string.count(character)
    #print(f"The character '{usr_char}' appears {result} times(s) in '{usr_str}'.")
    #I originally had the above line in the function itself but realized the instructions wanted the code structured so the returned count was then printed outside of the function. 
    #That makes sense because I may just want the returned value to use later and not have it always printed.
    return count
    
total_count = char_count(usr_str, usr_char)
    
print(f"The character '{usr_char}' appears {total_count} times(s) in '{usr_str}'.")