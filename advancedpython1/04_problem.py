try:
    a = input("Enter the Number: ")
    n = input("Enter the Number: ")
    print(int(a) / int(n))
except ZeroDivisionError as e:
    print("Infinite")
