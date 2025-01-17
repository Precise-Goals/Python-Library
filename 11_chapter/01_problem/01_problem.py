str = input("Word to find in file: ").lower()
with open("poems.txt") as f:
    if(str in f.read().lower()):
        print("Yes",str,"is present in poems.txt")
    else:
        print("No",str,"is not present in poems.txt")