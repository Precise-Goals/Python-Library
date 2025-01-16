def avg():
    a = int(input("Enter the a: "))
    b = int(input("Enter the b: "))
    c = int(input("Enter the c: "))
    average = (a+b+c)/float(3.0)
    print(average)


avg()
avg()

def greet(name = "User"):
    print("good day",name)

name = (input("Enter the Name: "))
greet(name)
greet()
