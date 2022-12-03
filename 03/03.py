# Day 3: Rucksack Reorganization

"""
length of string / 2
string indexes?
compare strings, find same item type (letter, case sensitive)
tranform letter into priority value (a-z: 1-26, A-Z: 27-52)
calculate sum of priorities
"""

test = "HelloaWörLda"
itemtypes = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

halfIndex = int(len(test)/2)
# print(int(len(test)/2))
compt1 = test[:halfIndex]
compt2 = test[halfIndex:]
itemtype = ""

prio = 0

found = False

print(compt1)
print(compt2)

for item1 in compt1:
    for item2 in compt2:
        if item1 == item2:
            found = True
            print("Found")
            itemtype = item1
            print(itemtype)
            break
        else:
            continue
    if found == True:
        found = False
        break



for i in range(len(itemtypes)):
    if itemtype == itemtypes[i]:
        prio = i+1
        print(prio)
        break