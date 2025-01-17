import os

with open("old.txt") as f:
    c = f.read()
os.remove("old.txt")
with open("new.txt", "w") as f:
    f.write(c)


'''    
old.txt contained...
A paragraph is a group of 
sentences that organizes 
a single idea in a 
written or spoken piece. 
Paragraphs can be 
used to develop a point, present 
the words of a speaker, or break up a 
text into manageable sections.
'''
