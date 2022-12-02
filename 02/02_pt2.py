# Day 2: Rock Paper Scissors
# Part 2

# open input file
input = open(r"02/input2.txt", encoding="utf-8")

"""
Encryption:

opponent:
rock     A
paper    B
scissors C

X lose => 0
Y draw => 3
Z win  => 6

points from shape:
rock (r)     => 1
paper (p)    => 2
scissors (s) => 3

Conditions:

loses: 0 + ?
A X => s 3
B X => r 1
C X => p 2

draws: 3 + ?
A Y => r 1
B Y => p 2
C Y => s 3

wins: 6 + ?
A Z => p 2
B Z => s 3
C Z => r 1

"""

total_score = 0

# test file
for line in input:
    if line[2] == "X":
        if line[0] == "A":
        # total_score += 0
            total_score += 3
        elif line[0] == "B":
            total_score += 1
        elif line[0] == "C":
            total_score += 2

    if line[2] == "Y":
        total_score += 3
        if line[0] == "A":
            total_score += 1
        elif line[0] == "B":
            total_score += 2
        elif line[0] == "C":
            total_score += 3

    if line[2] == "Z":
        total_score += 6
        if line[0] == "A":
            total_score += 2
        elif line[0] == "B":
            total_score += 3
        elif line[0] == "C":
            total_score += 1
            
print(total_score)

# close file
input.close()