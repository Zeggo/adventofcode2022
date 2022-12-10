# Part 2: What is the highest scenic score for any tree?
# Scenic score: multiplying the viewing distances in four directions
# Viewing distance: How many trees can be seen, stopping at a tree that is the same height or taller

#input_file = open(r"08/test_input8.txt", encoding="utf-8") # Test input

input_file = open(r"08/input8.txt", encoding="utf-8")
input = input_file.readlines()
input_file.close()
for i in range(len(input)):
    input[i] = input[i].rstrip()

best_score = 0

for y in range(len(input)):
    for x in range(len(input[y])):
        
        l = 0
        r = 0
        u = 0
        d = 0
        score = 0

        # Edge trees:
        if y == 0 or y == len(input)-1 or x == 0 or x == len(input[y])-1:
            score = 0
        
        # Interior trees:
        else:
            # Check left
            for i in range(x-1, 0-1, -1): # Starting from tree to the left
                if input[y][x] > input[y][i]: l += 1
                else:
                    l += 1
                    break

            # Check right
            for i in range(x+1, len(input[y])):
                if input[y][x] > input[y][i]: r += 1
                else:
                    r += 1
                    break

            # Check up
            for i in range(y-1, 0-1, -1): # Starting from tree upwards
                if input[y][x] > input[i][x]: u += 1
                else:
                    u += 1
                    break
            
            # Check down
            for i in range(y+1, len(input)):
                if input[y][x] > input[i][x]: d += 1
                else:
                    d += 1
                    break
            
        score = l * r * u * d

        if score > best_score:
            best_score = score
            print("Tree", y, x, "is now the best tree, with score", score)

print("The highest scenic score is:", best_score)