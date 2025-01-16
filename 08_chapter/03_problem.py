n = int(input("Enter the Number: "))


def sum(n):
    if (n == 0):
        return 0
    print(n)
    return n + sum(n-1)


print("Sum of", n, "is", sum(n))
