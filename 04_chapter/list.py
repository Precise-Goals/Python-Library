# lists are containers to set any kind of data types
list = [64, 23.523, "Hello world", True]
print(list[1])
print(list[3])
print(list[0])
list[0] = 128
print(list[0])
print(list[0:])
print(list[0:3])

s = [1, 4, 6, 2, 3, 5, 9, 8, 7]
print(s)
s.sort()
print(s)  # value changes
s.append(10)
print(s)  # value changes
s.reverse()
print(s)  # value changes
s.pop(2)
print(s)  # value changes
s.insert(4, 64)
print(s)  # value changes
s.remove(7)
print(s)  # value changes

'''
[1, 4, 6, 2, 3, 5, 9, 8, 7]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
[10, 9, 7, 6, 5, 4, 3, 2, 1]
[10, 9, 7, 6, 64, 5, 4, 3, 2, 1]
[10, 9, 6, 64, 5, 4, 3, 2, 1]
'''
