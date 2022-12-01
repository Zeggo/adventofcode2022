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

# Part 1: Compare values in list, find biggest value (max)
print("The elf carrying the most calories is carrying", max(elves), "Calories.")

# Part 2: Find the top three elves carrying the most Calories, count the total

# sort the list, find top three, calculate the sum
elves.sort(reverse=True)
total_calories_of_top_elves = sum(elves[0:3])

print("The top three elves are carrying", elves[0], "and", elves[1], "and", elves[2], "Calories on them.")
print("In total, they are carrying", total_calories_of_top_elves, "Calories.")

input.close()