class Emp:
    def __init__(self):
        print("Constructor of Employee")
    a = 1


class pg(Emp):
    def __init__(self):
        super().__init__()  # runs constructor of parent of this class
        print("Constructor of Programmer")
    b = 2


class mg(pg):
    def __init__(self):
        super().__init__()  # runs constructor of parent of this class
        print("Constructor of Manager")
    c = 3


# o = Emp()
# print(o.a)
# o = pg()
# print(o.a, o.b)

# we want parent constructor to work with derived one
o = mg()
print(o.a, o.b, o.c)
