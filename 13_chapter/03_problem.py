class Employ:
    salary = 234
    increment = 20

    @property
    def salaryAfterIncrement(self):
        return self.salary * (1 + (self.increment/100))

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, salary):
        self.increment = ((salary/self.salary) - 1) * 100


g = Employ()
# g.salary = 600000
# g.increment = 60
g.salaryAfterIncrement = 280
print(g.increment)
