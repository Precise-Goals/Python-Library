
def main():
    try:
        a = int(input("Hey, provide the number: "))
        print(a, "is a Integer")
        return a

    except Exception as e:
        print("Provide Valid Input")

    finally:
        print("Thank You, Finally is here")

    print("This will work hopefully")


main()
