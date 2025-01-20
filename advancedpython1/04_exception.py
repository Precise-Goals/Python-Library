try:
    a = int(input("Hey, provide the number: "))
    print(a, "is a Integer")
except ValueError as v:
    print(v)
except Exception as e:
    # print(e) print the error
    print("Provide Valid Input")

print("Thank You")


a = int(input("Enter 1st Number: "))
b = int(input("Enter 2nd Number: "))

if (b == 0):
    raise ZeroDivisionError("Program not meant to divide by zero")
# crash the program main stuff while buildig a python module
else:
    print("The Division a/b is", a/b)

try:
    a = int(input("Hey, provide the number: "))
    print(a, "is a Integer")
    
# if try successfully runs ->  else will execute
# try fails then respective exception occurs 

except Exception as e:    
    # print(e) print the error
    print("Provide Valid Input")
else:
    print("Thank You")
