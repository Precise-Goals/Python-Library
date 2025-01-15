name = "Sarthak patil"
#       012345....
# from ending -1 -2 -3
print(name)
nameshort = name[0:7]
print(nameshort)
initial = name[0]
print(initial)

# str = string[indexStart:indexEnd]
surname = name[-5:-1]
print(surname)
print(name[8:12])
print(name[:13])
print(name[0:])
print(name[-5:])

str = "0123456789"
# 1: 6
# 123456
# 15
# 123456789
# 1 SKIP-4 5 SKIP-4 9
print(str[1:6:4])
print(str[1:10:4])
# 1 se 10 tak 4-4 jumps lagani hai

print(len(name))
print(name.endswith("ak"))  # checks whether string ends with given substring
print(name.endswith("il"))  # checks whether string ends with given substring
# checks whether string starts with given substring
print(name.startswith("Pa"))
# checks whether string starts with given substring
print(name.startswith("Sa"))

print(name.lower())
print(name.upper())
print(name.capitalize())
print(name.title())

spare = "  Bhai Maaf Karde Pliz  "
print(spare.strip())
print(spare.lstrip())
print(spare.rstrip())

print(name.count('a')) # counts the occurances of letter
print(name.find("thak"))

print(name.replace("patil","Tulsidas patil"))
