# tuple is immutable
a = ()
b = (1,7,2,2,24,3,6,7,9,4,2,57,7,85,2,24,5,7,8,4,3,5,6,6,8)

print(b.count(6))
print(b.count(8)) #count occurences
print(b.count(7))

print(b.index(85)) # find the first occurance from starting of tuple