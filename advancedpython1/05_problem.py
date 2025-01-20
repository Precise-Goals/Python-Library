while True:
    n = input("Enter the Number: ")
    if n > '0' and n.isnumeric():
        break
    else:
        print("provide positive integer")

table = [int(n) * (i + 1) for i in range(10)]

with open("Tables.txt", "a") as f:
    f.write(str(table) + "\n")
