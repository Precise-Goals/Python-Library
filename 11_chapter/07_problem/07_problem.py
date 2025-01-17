with open("log.txt") as f:
    c = f.readlines()
for l in c:
    f = 0
    if "python" in l.lower():
        f = c.index(l)
        print("Python word is present in content at line", f+1)
        break
else:
    print("Python word is not present in content")
