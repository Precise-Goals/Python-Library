while True:
    n = input("Enter the Number: ")
    if n > '0' and n.isnumeric():
        break
    else:
        print("provide positive integer")

table = [f"{int(n)} x {i} = {int(n) * i}" for i in range(11)]

for index, item in enumerate(table):
    print(table[index])
