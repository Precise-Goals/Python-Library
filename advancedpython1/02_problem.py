ls = [3, 44, 53, 43, 43, 43, 43, 433]

for index, item in enumerate(ls):
    if index == 3 - 1 or index == 5 - 1 or index == 7 - 1:
        print(f"Element at index {index} is {item}")
