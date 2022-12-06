# Day 6: Tuning Trouble
# From the datastream, find the marker: four/fourteen different characters in a row
# Return the value where the four different characters have been received for the first time
input_file = open(r"06/input6.txt", encoding="utf-8")
input = input_file.read()
input_file.close()

def find_unique_set(set_length, input):
    last_set = ""
    for i in range(set_length, len(input)):
        last_set = input[i - set_length:i]
        #print(last_set)
        if len(set(last_set)) == len(last_set):
            return i

print("Part 1: The start-of-packet marker is at location", find_unique_set(4, input))
print("Part 2: The start-of-message marker is at location", find_unique_set(14, input))