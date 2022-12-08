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
print(input)

visible_trees = 0

for y in range(len(input)):
    for x in range(len(input[y])):
        # edge trees:
        if y == 0 or y == len(input)-1 or x == 0 or x == len(input[y])-1:
            visible_trees += 1
        # interior trees:
        else:
            is_visible = False
            # check left
            for i in range(len(input[y][:x])):
                if input[y][x] > input[y][i]:
                    is_visible = True
                    break
            # check right
            for i in range(len(input[y][x+1:])):
                if input[y][x] > input[y][i]:
                    is_visible = True
                    break
            # check up
            for i in range(len(input[:y])):
                #print(input[i])
                pass

            # check down

            if is_visible == True:
                visible_trees += 1
    print(visible_trees)
