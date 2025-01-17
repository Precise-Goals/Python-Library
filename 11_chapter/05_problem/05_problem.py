l = ["Faraday's","Law","that","of"]

with open("file.txt") as f:
    c = f.read()
    print(c)
for i in l:
    c = c.replace(i,"####")

with open("file.txt","w") as f:
    f.write(c)
    print(c)
    
    
    
# Faraday's laws of electromagnetic induction are two fundamental laws that describe how electric currents and magnetic fields interact. Here they are:

# Faraday's First Law
# Faraday's First Law of Electromagnetic Induction states that a change in the magnetic environment of a coil of wire will induce an electromotive force (emf) in the coil. This induced emf is proportional to the rate of change of the magnetic flux.

# Faraday's Second Law
# Faraday's Second Law of Electromagnetic Induction states that the magnitude of the induced emf in a coil is directly proportional to the rate of change of magnetic flux through the coil.