input = open(r"01/input.txt", encoding="utf-8")

elves = []
calories = 0

for line in input:

    # If line has a number, add the number into x
    if line != "\n":
        calories += int(line)

    # If line is empty (\n), add value to list, return value to 0
    else:
        elves.append(calories)
        calories = 0        

    # continue?
    # print(line)

print(elves)

# compare values in list, find biggest value (max)

input.close()
