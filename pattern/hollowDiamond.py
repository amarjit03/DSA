def main():
    n = 4

    # Top
    for i in range(n):
        # Leading spaces
        for j in range(n - i - 1):
            print(" ", end="")

        print("*", end="")

        if i != 0:
            # Inner spaces
            for j in range(2 * i - 1):
                print(" ", end="")

            print("*", end="")

        print()


if __name__ == "__main__":
    main()