# Day 3: Rucksack Reorganization

"""
length of string / 2
string indexes?
compare strings, find same item type (letter, case sensitive)
tranform letter into priority value (a-z: 1-26, A-Z: 27-52)
calculate sum of priorities
"""

test = "HeLLoWörLd"

halfIndex = int(len(test)/2)
# print(int(len(test)/2))
compt1 = test[:halfIndex]
compt2 = test[halfIndex:]
itemtype = ""

print(compt1)
print(compt2)

for item1 in compt1:
    for item2 in compt2:
        if item1 == item2:
            print("Found")
            itemtype = item1
            break
        else:
            continue

print(itemtype)