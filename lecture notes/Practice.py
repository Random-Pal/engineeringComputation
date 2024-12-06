grade = float(input("What grade did you get? "))

if grade <= 60 and grade >= 35:
    print("You have failed the exam.")
elif grade > 60 and grade < 95:
    print("You have passed the exam")
elif grade >=95:
    print("You did pretty good!")
elif grade < 35:
    print ("You gotta retake the class :/")
else:
    print("THAT'S NOT POSSIBLE!")