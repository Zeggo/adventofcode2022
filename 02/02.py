# Day 2: Rock Paper Scissors
# open input file
input = open(r"02/input2.txt", encoding="utf-8")

"""
Points:

opponent:
rock     A
paper    B
scissors C

you:
rock     X => 1
paper    Y => 2
scissors Z => 3

lose => 0
draw => 3
win  => 6

Conditions:
wins:
C X => 6 + 1
A Y => 6 + 2
B Z => 6 + 3

draws:
A X => 3 + 1
B Y => 3 + 2
C Z => 3 + 3

loses:
B X => 0 + 1
C Y => 0 + 2
A Z => 0 + 3

"""

total_score = 0

# test file
for line in input:
    if line[2] == "X":
        total_score += 1

        if line[0] == "C":
            total_score += 6
        elif line[0] == "A":
            total_score += 3
        elif line[0] == "B":
            continue

    if line[2] == "Y":
        total_score += 2
        if line[0] == "A":
            total_score += 6
        elif line[0] == "B":
            total_score += 3
        elif line[0] == "C":
            continue

    if line[2] == "Z":
        total_score += 3
        if line[0] == "B":
            total_score += 6
        elif line[0] == "C":
            total_score += 3
        elif line[0] == "A":
            continue

print(total_score)

# close file
input.close()