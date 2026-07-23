students = [
    ("Yash", 90),
    ("Rahul", 80),
    ("Amit", 90),
    ("Neha", 75),
    ("Priya", 80),
    ("Rohan", 75),
    ("Karan", 95)
]

def sort_students_by_marks(students):
    sorted_students = {}
    for student in students:
        if student[1] not in sorted_students:
            sorted_students[student[1]] = []
            sorted_students[student[1]].append(student[0])
        else :
            sorted_students[student[1]].append(student[0])
    return sorted_students

obj = sort_students_by_marks(students)
print(obj)
