l = [6, 7, 8, 9, 10]

for i in l:
    print(f"The item at index {l.index(i)} is {i}")


for index, item in enumerate(l):
    print(f"The item at index {index} is {item}")


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for i in list1:
#     sqList.append(i * i)

sqlist = [i * i for i in list1]


print(list1)
print(sqlist)
