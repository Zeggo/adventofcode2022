# Day 7: No Space Left On Device
# Browse the filesystem: directories and files with filesizes
# Determine the total size of each directory
# Find the directories with a total size of max. 100 000
# Find the sum of the total sizes of those directories
"""
Test input = ""$ cd /
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
7214296 k""
"""

# Create Dir class
# - has a name
# - includes files with names and sizes
# - includes directories with total sizes
# - calculate total size of directory

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