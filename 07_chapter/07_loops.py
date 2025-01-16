n = int(input("Enter the Number: "))
for i in range(n):
    if i % 2 != 0:
        continue
    for j in range(1, ((n-i)/2).__ceil__()):
        print("  ", end="")
    for j in range(i + 1):
        print("* ", end="")
    print("")
