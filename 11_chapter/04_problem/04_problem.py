str = input("Enter the word to Replace: ")
with open("faraday.txt") as f:
    content = f.read()
nv = content.replace(str,"#####")
print(nv)
with open("faraday.txt","w") as f:
    f.write(nv)
    
# Faraday's laws of electromagnetic induction are two fundamental laws that describe how electric currents and magnetic fields interact. Here they are:

# Faraday's First Law
# Faraday's First Law of Electromagnetic Induction states that a change in the magnetic environment of a coil of wire will induce an electromotive force (emf) in the coil. This induced emf is proportional to the rate of change of the magnetic flux.

# Faraday's Second Law
# Faraday's Second Law of Electromagnetic Induction states that the magnitude of the induced emf in a coil is directly proportional to the rate of change of magnetic flux through the coil.