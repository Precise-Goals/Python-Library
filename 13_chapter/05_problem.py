class Vec:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __add__(self, b):
        return Vec(self.a + b.a, self.b + b.b, self.c + b.c)

    def __mul__(self, b):
        return (self.a * b.a) + (self.b * b.b) + (self.c * b.c)

    def __str__(self):
        return f"{self.a}i + {self.b}j+ {self.c}k"


a = Vec(4, 5, 6)
b = Vec(1, 4, 9)

print(a + b)
print(a * b)
