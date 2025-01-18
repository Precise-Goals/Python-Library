class Emp:
    a = 1

    @classmethod
    def show(self):
        print(f"value of a is {self.a}")


e = Emp()
e.a = 45
e.show()

# for getting class Attribute


class Empe:
    a = 1

    @property  # getter
    def name(self):
        return f"{self.fname} {self.lname}"

    @name.setter  # setter
    def name(self, val):
        self.fname = val.split(" ")[0]
        self.lname = val.split(" ")[1]


e = Empe()
e.name = "Mark Zuckerberg"
print(e.fname,e.lname)

# encapsulation mhanje hidden methods la pack karne
# abstraction mahne hide karne

# for getting class Attribute
