from random import randint

numbers = tuple(randint(1, 20) for _ in range(5))

bestMatch = 0
i = 1
while i <= 5:
    # I originally had this without the map, int and split and it just gave me a tuple of strings with spaces between them. I forgot that input always returns a string and tuple usually just puts the information into a tuple and doesn't convert the individual elements. 
    nums = tuple(map(int, input(f"Attempt {i}: Enter 5 numbers between 1 and 20: ").split()))

    if nums == numbers:
        print("You guessed correctly!")
        break
    else:
        matches = 0

        for guess, answer in zip(nums, numbers):
            if guess == answer:
                matches += 1

        print(f"{matches} numbers matched in the correct position.")

        if matches > bestMatch:
            bestMatch = matches
    
    i += 1
if nums != numbers:
    print(f"Sorry! The correct combination was: {numbers}")
    print(f"Your best match was {bestMatch * 20}%.")
