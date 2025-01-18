class Number:
    def __init__(self, n):
        self.n = n

    def __add__(self, n):
        return self.n + n.n

    def __sub__(self, n):
        return self.n - n.n

    def __mul__(self, n):
        return self.n * n.n

    def __truediv__(self, n):
        return self.n / n.n

    def __floordiv__(self, n):
        return self.n // n.n


n = Number(1)
m = Number(2)

print(n + m)  # Output: 3
print(n - m)  # Output: -1
print(n * m)  # Output: 2
print(n / m)  # Output: 0.5
print(n // m) # Output: 0
