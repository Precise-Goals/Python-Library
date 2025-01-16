n = int(input("Enter the Number: "))


def pat(n):
    for i in range(n):
        for j in range(n-i):
            print("* ",end="")
        else:
            print("")
pat(n)