import wikipedia

print("Enter the Search: ",end="")
sear = input("")
res = wikipedia.summary(sear)
n = wikipedia.page(sear)
print(n.title)
print(n.content)
print(n.url)
wikipedia.set_lang("hi")
wikipedia.summary(sear)
print(res)


# Documentation : https://pypi.org/project/wikipedia/ 