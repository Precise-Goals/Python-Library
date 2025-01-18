class Complex:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, b):
        return Complex(self.x + b.x, self.y + b.y)

    def __mul__(self, b):
        real = (self.x * b.x) - (self.y * b.y)
        img = (self.x * b.y) + (self.y * b.x)
        return Complex(real, img)

    def __str__(self):
        return f"{self.x} + {self.y}i"


a = Complex(3, -2)
b = Complex(3, 2)
print(a + b)
print(a * b)

# '''𝑧1⋅𝑧2=(𝑎𝑐−𝑏𝑑)+(𝑎𝑑+𝑏𝑐)𝑖'''
# '''
# 𝑧1=𝑎+𝑏𝑖
# 𝑧2=𝑐+𝑑𝑖
# '''
