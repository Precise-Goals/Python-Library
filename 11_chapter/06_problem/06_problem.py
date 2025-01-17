with open("log.txt") as f:
    c = f.read().lower()
if 'python' in c:
    print("yes, Python is in this Content")
else:
    print("No, Python is not in this Content")