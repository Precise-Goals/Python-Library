class Animals:
    def __init__(self):
        print("Bhow Bhow")


class Pets(Animals):
    def __init__(self):
        super().__init__()


class Dogs(Pets):
    def __init__(self):
        super().__init__()

    @staticmethod
    def bark():
        print("Bhow Bhow")


d = Dogs()
d.bark()
