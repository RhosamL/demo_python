
#opening a file and read data: .open() May have to specify the path
#It is important to close file with .close()

#Main one is with open(The file you want to open) as (variable name)

#To divide a string to pieces: .split()
#Can split with "," or whitespace, etc.

#To clean up a variable: .strip()

with open("courses.txt") as course_file:
    for line in course_file:
        parts = line.split(",")
        print(line)
        print(parts[1])