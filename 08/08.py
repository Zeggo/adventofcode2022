# Day 8: Treetop Tree House
# Grid of trees heights 0-9
# Trees around the edge are visible
# Interior tree is visible if the trees between it and the edges are shorter than it
# Part 1: "How many trees are visible from outside the grid?"

test_input = """30373
25512
65332
33549
35390"""

input = test_input.split("\n")
#print(input)

visible_trees = 0

for y in range(len(input)):
    for x in range(len(input[y])):
        direction = []

        # Edge trees:
        if y == 0 or y == len(input)-1 or x == 0 or x == len(input[y])-1:
            visible_trees += 1
            #print("tree at", y, x, "is visible")
        
        # Interior trees:
        else:
            is_visible = False
            # Check left
            for i in range(len(input[y][:x])):
                if input[y][x] > input[y][i]:
                    is_visible = True
                else: is_visible = False
            if is_visible == True: direction.append("left")

            if is_visible == False:    
                # Check right
                for i in range(x, len(input[y][x+1:])):
                    if input[y][x] > input[y][i]:
                        is_visible = True
                    else: is_visible = False
                if is_visible == True: direction.append("right")

                if is_visible == False:        
                    # Check up
                    for i in range(len(input[:y])):
                        if input[y][x] > input[i][x]:
                            is_visible = True
                        else: is_visible = False
                    if is_visible == True: direction.append("up")
                    
                    if is_visible == False:
                        # Check down
                        for i in range(y, len(input[y+1:])):
                            if input[y][x] > input[i][x]:
                                is_visible = True
                            else: is_visible = False
                        if is_visible == True: direction.append("down")

            if is_visible == True:
                visible_trees += 1
                print("tree at", y, x, "is visible from", direction)

        #print("trees when x =", x, "is:", visible_trees)
    #print("at y =", y, "there are", visible_trees)

print("Total visible trees:", visible_trees)

"""
y = 3
x = 1

check up:
[0][1] => y-3, x
[1][1]
[2][1]




check down:
input[2:][1]

error in y = 3, x = 1 or 3
"""