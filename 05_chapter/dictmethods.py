marks = {
    "Chomu": 99,
    "Topper": 89,
    "Backbencher": 35.5,
    "list": [42, 5, 33, 11, 0]
}
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Chomu": 75, "Anonymous": 99})
print(marks.items())
print(marks.get("Mine")) # output none
# print(marks["Mine"]) # gives error
marks.pop("list")
print(marks.items()) # gives error
marks.popitem()
print(marks.items()) # gives error
