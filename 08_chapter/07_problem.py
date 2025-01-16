list = ["claude", "GPT", "Blackbox", "LightxEditor", "Gemini"]
# w = input("Word to remove: ")


def rem(l, w):
    print(l)
    n = []
    for item in l:
        if item != w:
            n.append(item.strip(w))
    return n


print(rem(list, "Gemini"))
