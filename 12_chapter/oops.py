class Employee:
    name = "Sarthak"
    language = "C++"
    salary = 1000000

    def __init__(self, name):  # is a constructor automatically runs
        self.name = name

    # __ dunder methods 
    # __ methods automatically calls

    @staticmethod
    def greet():
        print("Welcome to Newton.Co Industries...")

    def getInfo(self):
        print(f"{self.name} with {self.language} has {self.salary}/-")
        print(f"amount of salary with {self.experience} of experience")

# to hide the methods class uses abstraction and encapsulation


def show(new):
    print(" ")
    print("--------------------------")
    new.greet()
    print("--------------------------")
    new.getInfo()
    print("--------------------------")


new = Employee("Sarthak Tulsidas patil")
new.experience = "2 years"
# we can create objects
new.language = "CSS, Javascript"  # instance Attribute
# updates to instance attribute
print(new.name, new.language, new.salary, new.experience)

show(new)

# new.getInfo() = > Employee.getInfo(harry)
# isiliye we use self

