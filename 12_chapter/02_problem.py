import math


class Calculate:
    @staticmethod
    def greet(user):
        print(f"Hello, {user}")
    
    def Square(self, n):
        return math.pow(n, 2)

    def Cube(self, n):
        return math.pow(n, 3)

    def sqrt(self, n):
        return math.pow(n, 0.5)


j = int(input("Enter the Number: "))
u = input("Your Good Name: ")
n = Calculate()
n.greet(u)
print("Square: ", n.Square(j))
print("Sqrt: ", n.sqrt(j))
print("Cube: ", n.Cube(j))
