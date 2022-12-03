# Day 3: Rucksack Reorganization

"""
length of string / 2
string indexes?
compare strings, find same item type (letter, case sensitive)
tranform letter into priority value (a-z: 1-26, A-Z: 27-52)
calculate sum of priorities
"""

test = "HelloWorld"
halfIndex = int(len(test)/2)
# print(int(len(test)/2))
print(test[:halfIndex])
print(test[halfIndex:])