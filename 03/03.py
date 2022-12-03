# Day 3: Rucksack Reorganization

"""
length of string / 2
string indexes?
compare strings, find same item type (letter, case sensitive)
tranform letter into priority value (a-z: 1-26, A-Z: 27-52)
calculate sum of priorities
"""

input = open(r"03/input3.txt", encoding="utf-8")
#input = ["vJrwpWtwJgWrhcsFMMfFFhFp", "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", "PmmdzqPrVvPwwTWBwg", "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn", "ttgJtRGJQctTZtZT", "CrZsJsPPZsGzwwsLwLmpwMDw"]
itemtypes = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
itemtype = ""

prio_sum = 0

for line in input:

    half_index = int(len(line)/2)
    #print(int(len(test)/2))
    compt1 = line[:half_index]
    compt2 = line[half_index:]

    print(compt1)
    print(compt2)

    for item1 in compt1:
        found = False

        for item2 in compt2:

            if item1 == item2:
                found = True
                itemtype = item1
                print(itemtype)
                break

        if found == True:
            break

    for i in range(len(itemtypes)):
        if itemtype == itemtypes[i]:
            prio_sum += i+1
            break

print(prio_sum)

input.close()