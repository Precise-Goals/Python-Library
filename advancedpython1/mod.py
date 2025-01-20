def myFunc():
    print("Hello world")
    
myFunc()
print(__name__) # gives __main__


if __name__ == "__main__":
    print("Process under __main__")
    myFunc()
    myFunc()
    myFunc()
if __name__ == "mod":
    print("Process under mod module")
    myFunc()
    myFunc()