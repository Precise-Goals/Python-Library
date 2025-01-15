eng = int(input("English marks: "))
math = int(input("Maths marks: "))
sst = int(input("SST marks: "))
if ((eng > 33) and (math > 33) and (sst > 33)):
    total = ((eng+math+sst) / float(3))
    if(total>40):
        print("Student is Passed.")
    else:
        print("Student is failed.")
else:
    print("Student is failed in one of the Subject.")
