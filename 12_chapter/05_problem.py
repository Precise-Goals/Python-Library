from random import randint


class Train:

    def __init__(self, no):
        self.tNo = no

    def book(anything, fro, to):
        print(f"Ticket Booked for train no: {anything.tNo}") # problem 6 
        print(f"Journey: from {fro} to {to}")

    def getStatus(self):
        print(f"Train no {self.tNo} is Running on Time")

    def getFare(self, fro, to):
        print(f"Fare for train no {self.tNo}:", randint(400, 2400))
        print(f"Journey: from {fro} to {to}")


arr = input("Enter the Arrival station: ")
dest = input("Enter the Destination station: ")

t = Train(12455)
t.book(arr, dest)
t.getFare(arr, dest)
