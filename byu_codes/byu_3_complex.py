#Using complex conditionals, and or nor, etc.

#gpa = input("What is your GPA?: ")
#rgpa = float(gpa)

#if rgpa >= 0.85:
#    print("okay, kindly fill in your lowest grade point")
 #   lowest = input("fill in here: ")
  #  rlowest = float(lowest)
#    if rlowest >= 0.7:
#        print("you are a good student!")
#    elif rlowest < 0.7:
#        print ("You need to work harder.")
#
#else:
#    print("Your GPA is not up to the reguired theshold")

gpa = input("What is your cgpa?: ")
rgpa = float(gpa)

lowest = input("What is the lowest grade average you have had?: ")
rlowest = float(lowest)

#if rgpa >= 0.85 and rlowest >= 0.70:
#    print("Kindly submit your transcript to the department")
#else:
#    print("Your grade is not up to the mark required")
#Boolean flags
if rgpa > 0.5 and rlowest > 0.4:
    honour = True
else:
    honour = False

if honour:
    print("Call your HOD to schedule and meeting time")
if not honour:
    print("Sorry but we cannot meet with you at this moment")