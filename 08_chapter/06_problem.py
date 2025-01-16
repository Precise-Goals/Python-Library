def Table(n, i=1):
    if (i == 11):
        return 1
    print(n, "x", i, "=", n*i)
    return i + Table(n, i+1)


Table(5)
