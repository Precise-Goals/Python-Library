text = input("comment: ").lower()

if ((text.find("make a lot of money")) or (text.find("buy now")) or (text.find("subscribe this")) or (text.find("click this"))):
    print("Don't Spam your message.")
else:
    print("Message is safe.")
