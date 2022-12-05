# Day 5: Supply Stacks

#input = ['move 1 from 2 to 1', 'move 3 from 1 to 3', 'move 2 from 2 to 1', 'move 1 from 1 to 2']


input_file = open(r"05/input5.txt", encoding="utf-8")

# Split the input into two
crates = []
procedure = []
split = False

for line in input_file:    
    if line == "\n":
        split = True
        continue
    if split == False:
        crates.append(line)
    if split == True:
        procedure.append([int(i) for i in line.split() if i.isnumeric()]) # Make a list that includes lists with the procedure numbers

input_file.close()

#print(crates[0])
#print("\n\n\nBREAK HERE\n\n\n")
#print(procedure)

# Columns to rows => lists
# columns in same places -> placement to list name
# row -> placement in list, at the end => add new items to [0], not replacing previous items

# Take a symbol (crate) every x characters in string and add to list[0] if it is whitespace, ignore
stacks = list(([],[],[],[],[],[],[],[],[]))

for row in range(len(crates)):
    stack_index = 0
    for column in range(1, len(crates[row]), 4):
        if crates[row][column].isalpha(): #crates[row][column] != " " or 
            stacks[stack_index].insert(0, crates[row][column])
        stack_index += 1

print(stacks)