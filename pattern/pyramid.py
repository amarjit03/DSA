def print_pyramid(n):

    # Outer loop for rows
    for i in range(1, n + 1):

        # Print spaces
        print(" " * (n - i), end="")

        # Print stars
        print("*" * (2 * i - 1))

if __name__=="__main__":
    n = 40
    print_pyramid(n)
