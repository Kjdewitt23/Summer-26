def numSer(start, end, step):
    nums = []
    for num in range(start, end, step):
        nums.append(num)
    with open("number_seies.txt", "w") as f:
        for num in nums:
            f.write(f"{num} \n")
    length = len(nums)
    print(f"Saved {length} numbers to number_series.txt")

# In general, I get the benefit to having the list before writing it to the file. But, for this script, wouldn't it be faster to just write the number immediately instead of storing it in a list first?

def main():
    start = int(input("Enter starting number: "))
    end = int(input("Enter ending number: "))
    step = int(input("Enter step size: "))

    numSer(start, end, step)

if __name__ == "__main__":
    main()
