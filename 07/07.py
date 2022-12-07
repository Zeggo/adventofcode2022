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
input = test_input.split("\n")
print(input)

# Create Dir class
# - has a name
# - includes files with names and sizes
# - includes directories with total sizes
# - calculate total size of directory
class Dir:
    def __init__(self, name, files) -> None:
        self.name = name
        self.files = files

    def calculate_total_size(self):
        total_size = 0
        for file in files:
            total_size += file["size"]

        print("Total size:", total_size)

# Create file dictionary
# Has a name as a string and a size as int
def create_file(filename, filesize):
    file = {
        "name": filename,
        "size": filesize
        }
    return file

files = []

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

for line in input:
    if line[0] == "$": # is command
        if line[2:3] == "cd":
            pass
