print(1)
print(2)
print(3)
print(4)
print(5)

for i in range(1, 6):
    print(i)

i = 0
while (i < 6):
    print(i)
    i += 1

i = 1
while (i <= 50):
    print(i)
    i += 1

while (True):
    S = input("Enter the name: ")
    if (S == "Sarthak"):
        print("Prototype Terminated")
        break

list = ["Something", "Got", "To", "Be", "Serious"]

i = 0
while (i < len(list)):
    print(list[i], " ")
    i += 1

for i in range(5):  # (0 to 4)
    print(list[i])

for i in range(0, 100, 10):  # (0 to 100 but only gives number after 10 steps)
    print(i)

for i in list:
    print(i)

t = (6, 23, 4, 2, 23)

for i in t:
    print(i)

name = "Sarthak"

for i in name:
    print(i)


# for - else
print("Printing List...")
for i in list:
    print(i)
else:
    print("List printing is done.")


i = 0
while (i < 80):
    print(i)
    if (i == 3):
        break
    i += 1

for i in range(1, 80):
    if ((i % 3 == 0) or (i % 5 == 0) or (i % 7 == 0)):
        continue
    else:
        print(i)
else: 
    print("sub prototype is executed.")

for i in range (0,5):
    pass # empty for loop