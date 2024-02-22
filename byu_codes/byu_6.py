#Opening and reading from files.

#Open by using the open function

with open("courses.txt") as courses_file:
    for line in courses_file:
        print(line)

#Cleaning strings

items = ("ballon phone iphone keypad")

item = items.split(",")
#['ballon', 'phone', 'iphone', 'keypad']
print(item)

for one_item in item:
    print(one_item)

#second = item[2]
#print(second)

cleaned_item = [x.strip() for x in item if x != ""]  #removes any empty spaces at the
