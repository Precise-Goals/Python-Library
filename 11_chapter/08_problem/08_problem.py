with open("f.txt") as f:
    c = f.read()
with open("n.txt","w") as f:
    f.write(c)