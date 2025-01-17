with open("s1.txt") as f:
    a = f.read()
with open("s2.txt") as f:
    b = f.read()

if a == b:
    print("Both files are Identical")
else:
    print("both files are not Identical")
