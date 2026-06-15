def split_even_odd(nums):
    even_nums = []
    odd_nums = [] 
    for num in nums:
        if num % 2 == 0:
            even_nums.append(num)
        else:
            odd_nums.append(num)
    return even_nums, odd_nums
    # I chose this loop method because it's always going to be the length of nums so a for loop works. It's also easy because if a number isn't even, it's odd. 

def main():
    sample = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    even_nums, odd_nums = split_even_odd(sample)
    # I needed to lookup more info about returning multiple values from one function. I'm not sure if there's a better way to do this or not. 

    print(f"Original list: {sample}")
    print(f"Odd values: {odd_nums}")
    print(f"Even values: {even_nums}")

if __name__ == "__main__":
    main()