def check(n):
    return True if int(n) % 2 == 0 else False
n = input("Enter the Number: ")
if check(n):
    print("Number is Even")
else:
    print("Number is odd")


