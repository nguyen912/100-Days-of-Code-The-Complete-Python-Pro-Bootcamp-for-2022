student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇
# Scores 91 - 100: Grade = "Outstanding"
# Scores 81 - 90: Grade = "Exceeds Expectations"
# Scores 71 - 80: Grade = "Acceptable"
# Scores 70 or lower: Grade = "Fail"
for student in student_scores:
    if student_scores[student] <= 70:
        student_grades[student] = "Fail"
    if 71 <= student_scores[student] <= 80:
        student_grades[student] = "Acceptable"
    if 81 <= student_scores[student] <= 90:
        student_grades[student] = "Exceeds Expectations"
    if 91 <= student_scores[student] <= 100:
        student_grades[student] = "Outstanding"

# 🚨 Don't change the code below 👇
print(student_grades)





