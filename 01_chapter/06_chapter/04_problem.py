username = input("enter the username: ").lower()
if(len(username)<10):
    print("username is valid")
else:
    print("username must be less than 10 characters")