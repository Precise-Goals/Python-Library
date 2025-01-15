s = set()
"""
This script demonstrates the usage of Python sets and some of their commonly used methods.
A set is an unordered collection of unique elements. Sets are mutable, meaning that you can add or remove elements after the set has been created.
The following methods are demonstrated in this script:
- add(element): Adds an element to the set. If the element is already present, it does nothing.
- remove(element): Removes the specified element from the set. Raises a KeyError if the element is not found.
- pop(): Removes and returns an arbitrary element from the set. Raises a KeyError if the set is empty.
- clear(): Removes all elements from the set, leaving it empty.
Example usage:
    print(s)  # Output: {32, 34}
    s.add(32)  # No effect, as 32 is already in the set
    s.add(34)  # No effect, as 34 is already in the set
    print(s)  # Output: {32, 34}
    print(s)  # Output: {34}
    print(s)  # Output: {34, 50}
    print(s)  # Output: {50} or {34}, depending on which element was popped
    print(s)  # Output: set()
"""
s.add(32)
s.add(34)
print(s)
# collection of non repetitive elements
s.add(32)
s.add(34)
print(s)

# Demonstrating some set methods
s.remove(32)  # Removes element 32 from the set
print(s)

s.add(50)  # Adds element 50 to the set
print(s)

print(s.pop())  # Removes and returns an starting element from the set
print(s)

s.clear()  # Removes all elements from the set
print(s)


'''Sets are unorderred, unindexed, no way to change the items, cannot set duplicate values'''

SSS = {2, 4, 6, 8, 10}
print(len(SSS))
SSS.pop()
print(SSS)
SS = {1, 2, 3, 5, 6, 7, 9}
print(SSS.intersection(SS))
print(SSS.union(SS))
