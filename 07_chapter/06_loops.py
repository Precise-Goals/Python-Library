fact = 1
n = int(input("Enter the Number: "))
for i in range(1, n+1):
    fact *= i
else:
    print("The Factorial of ", n, "is", fact)
