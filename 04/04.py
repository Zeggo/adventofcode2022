# Day 4: Camp Cleanup

import re

"""
tranform into set: sections 2-4 => 2, 3, 4
is one set a subset of the other or vice versa
"""
"""
input_file = open(r"04/input4.txt", encoding="utf-8")
input = input_file.readlines()
input_file.close()
"""
test = "2-4,3-10"
output = re.split("-|,", test)
print(output)

set1 = {*range(int(output[0]), int(output[1])+1, 1)}
print(set1)