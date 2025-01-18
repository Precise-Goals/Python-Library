class Vec:
    def __init__(self, list):
        self.l = list

    def __add__(self, b):
        return Vec(self.a + b.a, self.b + b.b, self.c + b.c)

    def __mul__(self, b):
        return (self.a * b.a) + (self.b * b.b) + (self.c * b.c)

    def __str__(self):
        return f"{self.a}i + {self.b}j+ {self.c}k"

    def __len__(self):
        return len(self.l)


v1 = Vec([9, 5, 4])
print(len(v1))
