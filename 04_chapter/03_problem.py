check = (1, 3, 54, 12, 34)
print(check[3])
check[3] = 21
print(check[3])
'''Traceback (most recent call last):
  File "d:\Workspace\Coding\projects\learn\python\04_chapter\03_problem.py", line 3, in <module>
    check[3] = 21
    ~~~~~^^^
TypeError: 'tuple' object does not support item assignment
'''
