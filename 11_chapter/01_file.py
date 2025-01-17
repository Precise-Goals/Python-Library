# RAM = Volatile data persist nahi karat data nahi tikat
# HDD = non volatile Data persist karte

emails = []

# programs start you filled this list program end your emails becomes empty
# storing data use non volatile mem
# ram mein temporarily load honda si
# ram is use for fast execution comparitivelyy than hdd/ssd

str = "Bhai sun, Chai pine chal\n"

f = open("file.txt", 'w')
# use 'a' for append
# 'rb' read in binary mode
# 'rt' open in text mode
# + updating
for i in range(5):
    f.write(str)
else:
    f.write("Batch Operation Completed")
f.close()
