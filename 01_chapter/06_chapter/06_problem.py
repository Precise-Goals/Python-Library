grade = float(input("Enter your accurate cgpa: "))
cgpa = grade*10
if ((cgpa >= 90) and (cgpa <= 100)):
    print("Passed with distinction")
elif ((cgpa >= 80)):
    print("Passed with A Grade")
elif ((cgpa >= 70)):
    print("Passed with B Grade")
elif ((cgpa >= 60)):
    print("Passed with C Grade")
elif ((cgpa >= 50)):
    print("Passed with D Grade")
else :
    print("Failed with E Grade")
