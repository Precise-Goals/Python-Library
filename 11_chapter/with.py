f = open("file.txt")
print(f.read())
f.close()

# same can be written using with statement

with open("file.txt") as f:
    print(f.read())