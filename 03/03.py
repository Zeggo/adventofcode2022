# Day 3: Rucksack Reorganization

"""
length of string / 2
string indexes?
compare strings, find same item type (letter, case sensitive)
tranform letter into priority value (a-z: 1-26, A-Z: 27-52)
calculate sum of priorities
"""

#input = open(r"03/input3.txt", encoding="utf-8")
input = ["vJrwpWtwJgWrhcsFMMfFFhFp", "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", "PmmdzqPrVvPwwTWBwg", "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn", "ttgJtRGJQctTZtZT", "CrZsJsPPZsGzwwsLwLmpwMDw"]
itemtypes = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
itemtype = ""

prio_sum = 0

for line in input:

    half_index = int(len(line)/2)
    #print(int(len(test)/2))
    compt1 = line[:half_index]
    compt2 = line[half_index:]

    #print(compt1)
    #print(compt2)

    for item1 in compt1:
        found = False

        for item2 in compt2:

            if item1 == item2:
                found = True
                itemtype = item1
                #print(itemtype)
                break

        if found == True:
            break

    for i in range(len(itemtypes)):
        if itemtype == itemtypes[i]:
            prio_sum += i+1
            break

print("Part 1:", prio_sum)

# Part 2
# compare three consecutive lines to find common badge item (letter)
# calculate sum of badge priorities
badge = ""
badge_sum = 0

for i in range(0, len(input), 3):
    for item1 in input[i]:
        found = False

        for item2 in input[i+1]:

            if item1 == item2:

                for item3 in input[i+2]:
                    if item1 == item3:
                        found = True
                        print(item1)
                        break

            if found == True:
                break

        if found == True:
            break



#input.close()