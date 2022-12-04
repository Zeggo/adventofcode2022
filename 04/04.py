# Day 4: Camp Cleanup

import re

"""
tranform into set: sections 2-4 => 2, 3, 4
is one set a subset of the other or vice versa
"""

input_file = open(r"04/input4.txt", encoding="utf-8")
input = input_file.readlines()
input_file.close()

#input = ["2-4,6-8", "2-3,4-5", "5-7,7-9", "2-8,3-7", "6-6,4-6", "2-6,4-8"] #test input

duplicate_assignments = 0
overlapping_assignments = 0

for line in input:
    # Splitting the input into a list
    sections = re.split("-|,", line)
    #print(sections)

    # Assignments of sections
    ass1 = {*range(int(sections[0]), int(sections[1])+1, 1)}
    ass2 = {*range(int(sections[2]), int(sections[3])+1, 1)}
    #print(ass1)
    #print(ass2)

    # Comparing if one set fully contains the other
    if ass1.issubset(ass2) or ass2.issubset(ass1):
        duplicate_assignments += 1

    if not(ass1.isdisjoint(ass2)):
        overlapping_assignments +=1

print(duplicate_assignments)
print(overlapping_assignments)