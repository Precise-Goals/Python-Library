def Pal(number):
    num = number
    return True if num == num[::-1] else False
num = input("Enter the Number: ")
if Pal(num):
    print("Number is Palindrome")
else:
    print("Number is not Palindrome")
    
