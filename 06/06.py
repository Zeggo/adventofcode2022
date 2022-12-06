# Day 6: Tuning Trouble
# From the datastream, find the marker: four different characters in a row
# Return the value where the four different characters have been received for the first time
input_file = open(r"06/input6.txt", encoding="utf-8")

input = input_file.read()

last_four = ""
for char in range(4, len(input)):
    last_four = input[char-4:char]
    print(last_four)
    if len(set(last_four)) == len(last_four):
        print(char)
        break
