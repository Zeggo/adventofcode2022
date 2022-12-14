# Day 7: No Space Left On Device
# Browse the filesystem: directories and files with filesizes
# Determine the total size of each directory
# Find the directories with a total size of max. 100 000
# Find the sum of the total sizes of those directories

test_input = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""
#input = test_input.split("\n")
#print(input)

input_file = open(r"07/input7.txt", encoding="utf-8")
input = input_file.readlines()
input_file.close()
for i in range(len(input)):
    input[i] = input[i].rstrip()

# Create Dir class
# - has a name and upper directory
# - includes files with names and sizes
# - includes directories with total sizes
# - calculate total size of directory
class Dir:
    def __init__(self, name, parent) -> None:
        self.name = name
        self.parent = parent
        self.children = []
        self.files = []

    def __str__(self) -> str:
        return f"I am directory {self.name} and my size is {self.calculate_total_size()}."

    def calculate_total_size(self):
        total_size = 0
        for file in self.files:
            total_size += file["size"]
        for child in self.children:
            total_size += child.calculate_total_size()

        return total_size

# Create file dictionary
# Has a name as a string and a size as int
def create_file(filename, filesize):
    file = {
        "name": filename,
        "size": filesize
        }
    return file

# Parse input:
# $ = command
#   cd = change directory
#       /   = root dir
#       ..  = out one level
#       x   = in one level to dir x
#   ls = list
#       => create files
#       dir x -> directory object, name
#       int y -> file size, name

upper_dir = None
current_dir = None
all_dirs = []

for line in input:
    
    if line[0] == "$": # is command
        #print(line)
        if line[:3+1] == "$ cd": # change directory
            
            if line[5] == "/": # root
                root = Dir("root", None)
                all_dirs.append(root)
                current_dir = root
            
            elif line[5:6+1] == "..": # out
                current_dir = upper_dir
                if upper_dir == root: upper_dir.parent = None
                else: upper_dir = upper_dir.parent

            else: # in
                upper_dir = current_dir
                for dir in upper_dir.children:
                    if line[5:] == dir.name:
                        current_dir = dir

        elif line[2:3+1] == "ls":
            pass

        #print(current_dir)
    
    else: # not a command, either dir or file listed after ls
        # Listed directory:
        if line[:2+1] == "dir":
            new_dir = Dir(line.split()[1],current_dir) # add directory
            #print(new_dir.name)
            current_dir.children.append(new_dir) # add directory as a child to current dir
            all_dirs.append(new_dir)

        # Listed file:
        else:
            new_file = create_file(line.split()[1], int(line.split()[0]))
            #print(new_file["name"])
            current_dir.files.append(new_file) # add file to current dir list of files

print("The total size of the root directory is:", root.calculate_total_size())

# Find small directories (at or below max size)
# Calculate the sum of total sizes of those directories
# Recursion

def calculate_sum_of_small_dirs_sizes(root, max_size):
    sum_of_small_dirs_sizes = 0
    for dir in root.children:
        if dir.calculate_total_size() <= max_size:
            sum_of_small_dirs_sizes += dir.calculate_total_size()
        calculate_sum_of_small_dirs_sizes(dir, max_size)
    return sum_of_small_dirs_sizes

max_size = 100_000

# No duplicates:
#print("The sum of sizes of small directories is:", calculate_sum_of_small_dirs_sizes(root, max_size))

# With duplicates:
sum_of_small_dirs_sizes = 0
for dir in all_dirs:
    if dir.calculate_total_size() <= max_size:
        sum_of_small_dirs_sizes += dir.calculate_total_size()

# Part 1 solution:
print("The sum of sizes of small directories is:", sum_of_small_dirs_sizes)

# Part 2:
# Find the smallest directory to delete for freeing up enough space
# Find the total size of that directory

disk_space = 70_000_000
update_size = 30_000_000

unused_space = disk_space - root.calculate_total_size()
required_space = update_size - unused_space
print("Currently unused space:", unused_space)
print("Still required space:", required_space)

smallest_dir_to_delete = root
for dir in all_dirs:
    dir_size = dir.calculate_total_size()
    if dir_size >= required_space: # The directory needs to be at least as big as the still required space
        if dir_size < smallest_dir_to_delete.calculate_total_size(): # Find the smallest suitable directory
            smallest_dir_to_delete = dir

# Part 2 solution:            
print("The smallest directory to delete says:", smallest_dir_to_delete)