try:
    with (
        open("1.txt") as f1,
        open("2.txt") as f2,
        open("3.txt") as f3
    ):
        f1.read()
        f2.read()
        f3.read()

except FileNotFoundError as e:
    print(e)
    print("File Cannot be found, kindly create them")

finally:
    print("File Cannot be found, kindly create them")
