verified = ["sarthak","Rafael","Simon","Carl","Tommy"]

name = input("Name: ").lower()
if(verified.count(name)):
    print("Name is in the List")
else: 
    print("Name is not in the List")