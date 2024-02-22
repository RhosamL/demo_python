#To print a student's grade
# A >= 90, B >= 80, C >= 70, D >= 60, F < 60.

grade = float(input("Please input yoyur grade percent: "))

if grade >= 90:
    letter = 'A'
elif grade >= 80:
    letter = 'B'
elif grade >= 70:
    letter = 'C'
elif grade >= 60:
    letter = 'D'
elif grade < 60:
    letter = 'F'
else:
    print("Invalid Grade!")
print(f"Your grade is {letter}")

ppass = "You passed the course. Kindly register for the next semester"
fail = 'Sorry! You failed this course'
if grade >= 70:
    print (ppass)
else:
    print(fail)

#Stretch Callnage
extra = grade % 10
if extra > 5:
    pletter = '+'
    if grade > 50:
        print(f"extra and grade {letter + pletter}")
if extra < 5 and grade >= 90:
    pletter = '-'