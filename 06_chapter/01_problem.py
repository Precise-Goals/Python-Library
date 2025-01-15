

numbers = set()
a = int(input("Enter the Number a: "))
b = int(input("Enter the Number b: "))
c = int(input("Enter the Number c: "))
d = int(input("Enter the Number d: "))
numbers.add(a)
numbers.add(b)
numbers.add(c)
numbers.add(d)

print(numbers)
if ((a > b) and (a > c) and (a > d)):
    print("a is the greatest number: ",a)
elif ((b > a) and (b > c) and (b > d)):
    print("b is the greatest number: ",b)
elif ((c > a) and (c > b) and (c > d)):
    print("c is the greatest number: ",c)
elif ((d > a) and (d > b) and (d > c)):
    print("d is the greatest number: ",d)