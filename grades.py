# Input the class score from the user
class_score = float(input("Enter the class score: "))

# Determining the grade based on the grading scheme used in the class
if class_score >= 90 and  class_score<=100:
    grade = 'A'
elif class_score >= 80 and class_score<90 :
    grade = 'B'
elif class_score >= 70 and class_score<80:
    grade = 'C'
elif class_score >= 60 and class_score<70:
    grade = 'D'
elif class_score <60:
    grade = 'F'
else:
    grade = 'Wrong Score'

# Print the grade
print("Grade:", grade)
