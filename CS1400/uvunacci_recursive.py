# Fibonacci sequence but uses previous 3 terms instead of 2
def uvunacci_recursive(n):
    if n <= 2:
        return n
    else:
        return uvunacci_recursive(n-1) + uvunacci_recursive(n-2) + uvunacci_recursive(n-3)

def main():

    # Prints out each term in UVUnacci sequence for range
    term_lst = [uvunacci_recursive(i) for i in range(30)]
    print("UVUnacci (first 30 terms): ")
    print(term_lst)

if __name__ == "__main__":
    main()