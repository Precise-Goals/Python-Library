import math

n = int(input("Enter the Number: "))
f = 0
for i in range(2, math.sqrt(n).__ceil__()):
    if (n % i == 0):
        f = 1
        break

if (f == 1):
    print("Number is not Prime")
else:
    print("Number is Prime")
