# Day 07 - working with text files

# Exercise 1: create names.txt with three names, one per line.
# "w" = write: creates the file, or EMPTIES it if it already exists.
with open("names.txt", "w") as file:
    file.write("Jack\nMike\nLisa\n")   # \n = new line, write() does not add it

# Exercise 2: read the whole file at once.
# "r" = read. read() returns everything as ONE string, newlines included.
with open("names.txt", "r") as file:
    text = file.read()
    print(text)         # 3 names + 1 empty line (the last \n plus print's own)
    print(repr(text))   # repr shows the hidden characters: 'Jack\nMike\nLisa\n'

# Exercise 3: read line by line and remove the newline with strip().
with open("names.txt") as file:
    for line in file:
        print(line.strip())   # 3 clean lines, no empty line

# Exercise 4: add a name at the end.
# "a" = append: adds at the end WITHOUT deleting what is already there.
with open("names.txt", "a") as file:
    file.write("Anna\n")

# readlines() returns a list with one element per line, len() counts them.
with open("names.txt") as file:
    print(len(file.readlines()))   # 4

# Exercise 5 (on purpose): "r" on a file that does not exist.
# It raises FileNotFoundError because "r" never creates files.
# Uncomment the next lines only to see the error again:
# with open("missing.txt", "r") as file:
#     print(file.read())