f = open("read.txt", 'r')
# f = open("read.txt") # same as  above line
print(" ")
for i in f.readlines():
    print(i, end="")
else:
    print(" ")
    print("\nErwin Smith from AOT")
# treat it like a list
print(" ")
f.close()

f = open("read.txt")
line1 = f.readline()  # once read cant read one more time
print(line1, end="")
line2 = f.readline()
print(line2, end="")
line3 = f.readline()
print(line3, end="")

f.close()

f = open("read.txt")
line = f.readline()
while (line != ""):
    print(line, end="")
    line = f.readline()
f.close()
