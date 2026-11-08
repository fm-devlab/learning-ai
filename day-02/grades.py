# Ask for a Swiss grade (1 to 6) and convert the answer to an integer
grade = int(input("Insert your grade: "))

# 6 is the best grade
if grade == 6:
    print("Excellent")
# Python checks the branches from top to bottom and stops at the first true one
elif grade == 5:
    print("Good")
elif grade == 4:
    print("Sufficient")
# Two conditions joined by "and": the grade must be below 4 AND above 0 (so 1, 2 or 3)
elif grade < 4 and grade > 0:
    print("Insufficient")
# Everything not caught above: 0, negative numbers and values over 6
else:
    print("Grade not valid")