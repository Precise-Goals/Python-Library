# arithmetic operator + - / *
# relational operator == != > < >= <=
# logical operator AND,OR, NOT
# assignment operator += -= =
a = 6 - 5 + 32
print(a)
b = 5
print(b)
b += 5
print(b)
b -= 2
print(b)

c = a > b
print(c)

# its note that output of input() is always string no matters number is entered
d = input("a: ")
"""Traceback (most recent call last):
  File "d:\Workspace\Coding\projects\learn\python\02_chapter\operators.py", line 19, in <module>
    print(d*d)
          ~^~
TypeError: can't multiply sequence by non-int of type 'str'"""
print(type(a))
e = "Parrot"
print(type(e))

print(int(d)*int(d))
