a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

S = set()
S.add(a)
print(S)
S.add(b)
print(S)
S.add(c)
print(S)


def large(a, b, c):
    if (a > b and a > c):
        return a
    elif (b > a and b > c):
        return b
    else:
        return c


print("Large number is c =", large(a, b, c))
