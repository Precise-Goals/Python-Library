class Employ:
    fern = "International Blockchain Services"

    def show(self):
        print(f"Employe {self.name} has {self.salary} amount of salary")


# class NinheritPg:
#     fern = "International Blockchain Management Systems"
#     def show(self):
#         print(f"Employe {self.name} has {self.salary} amount of salary")

#     def show(self):
#         print(f"Employe {self.name} is good with {self.lang} markup/language")

class Coder:
    def showLang(self):
        print(f"Employe {self.name} is good with {self.lang} markup/language")


class inheritPg(Employ, Coder):
    fern = "International Blockchain Management Systems"

    def Origin(self):
        print(f"Origin is {self.origin}")


class End (inheritPg):
    fern = "Internation Society for Blockchain Business Association"


em = Employ()
# npg = NinheritPg()
pg = inheritPg()

pg.name = "Sarthak"
pg.salary = 43344443
pg.lang = "Rust, C#, Java, CSS, HTML"
pg.show()
pg.showLang()

print(em.fern)
print(pg.fern)


j = End()
j.name = "Kid"
j.salary = 6000
j.lang = "Rust, Pocket Money"
j.origin = "ohio, Florida"


j.show()
j.showLang()
j.Origin()

# single inheritance
# base -> derived

# multiple inheritance
# base 1            base2
#  |__________________|
#           |
#        Derived

# multilevel inheritance
#         Base
#          |
#       Derived 1
#          |
#       Derived 2
