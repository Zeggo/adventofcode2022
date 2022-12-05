# Day 5: Supply Stacks

#input = ['move 1 from 2 to 1', 'move 3 from 1 to 3', 'move 2 from 2 to 1', 'move 1 from 1 to 2']


input_file = open(r"05/input5.txt", encoding="utf-8")

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
        procedure.append(line.split( )) # Make a list that includes lists with the procedure numbers in indexes 1, 3 and 5

input_file.close()

#print(crates)
#print("\n\n\nBREAK HERE\n\n\n")
print(procedure)

numbers = [i for i in input if i.isnumeric()]
#print(numbers)