# Day 6: Tuning Trouble
# From the datastream, find the marker: four different characters in a row
# Return the value where the four different characters have been received for the first time
input_file = open(r"06/input6.txt", encoding="utf-8")
input = input_file.read()
input_file.close()


# Part 1: Find the start-of-packet marker with four distinct characters
last_four = ""
for char in range(4, len(input)):
    last_four = input[char-4:char]
    #print(last_four)
    if len(set(last_four)) == len(last_four):
        print("Part 1: The start-of-packet marker is at location", char)
        break

# Part 2: Find the start-of-message marker with fourteen distinct characters
last_fourteen = ""
for char in range(14, len(input)):
    last_fourteen = input[char-14:char]
    #print(last_fourteen)
    if len(set(last_fourteen)) == len(last_fourteen):
        print("Part 2: The start-of-message marker is at location", char)
        break