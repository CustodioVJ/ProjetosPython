student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}

#pegando os valores dos dicionarios
for s in student_scores:
    score = student_scores[s]
    if score > 90:
        student_grades[s] = "Outstanding"
    elif score > 80:
        student_grades[s] = "Exceeds Expectations"
    elif score > 70:
        student_grades[s] = "Acceptable"
    else:
        student_grades[s] = "Fail"

print(student_grades)
