from functools import reduce

S = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sq = map(lambda x: x * x, S)

print(S)
print(list(sq))


def even(n):
    return True if n % 2 == 0 else False


print(list(filter(even, S)))


def add(a, b):
    return a + b


print(reduce(add, S))
