from mod import myFunc
# gives  __moduleName__


a = 5


def fun():
    global a
    a = 3
    print(a)


fun()
print(a)
