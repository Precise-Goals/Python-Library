'''
Write a program to fill in a letter template given below with name and date.
letter = 
Dear <|Name|>,
You are selected!
<|Date|>
'''
Name = input("Enter the Name: ")
Date = input("Enter the Date: ")
print("Dear", Name, "\nYou are selected!", "\n", Date)
