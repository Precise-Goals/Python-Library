print("-----------------------")
print("Welcome to Newton.Co...")
print("-----------------------")


def assign(self, i):
    v = ""
    v += "-----------------------\n"
    v += "Employee id " + str(i+641) + ": " + "\n"
    v += "           Name |- " + self.name + "\n"
    v += "         Salary |- " + str(self.salary) + "\n"
    v += "       Language |- " + self.languages + "\n"
    v += "         Origin |- " + self.origin + "\n"
    v += "     Experience |- " + str(self.exp) + "\n"
    with open("data.txt", 'a') as f:
        f.write(v)


class Emp:
    name = ""
    salary = 0
    exp = 0
    languages = ""
    origin = ""

    def dataStoring(self, i):
        assign(self, i)

    def dataPrinting(self, i):
        print("Data Stored for employee", self.name, "with emp_id ", i + 641)
        # our company starts with 2^6 * 10


n = int(input("How many Employees to Add: "))
employees = [Emp() for i in range(n)]

for i in employees:
    print("-----------------------")
    i.name = input("Enter the Name: ")
    i.salary = input("Enter the Salary: ")
    i.exp = input("Enter the years of exp: ")
    i.languages = input("Enter the Languages: ")
    i.origin = input("Enter the Origin Country: ")


print("-----------------------")
print("Storing Data Entries")

for emp in employees:
    emp.dataStoring(employees.index(emp))
    emp.dataPrinting(employees.index(emp))
else:
    print("-----------------------")
    print("Data Has Been Stored...")
    print("-----------------------")
