# Student data
students = ["Ravi", "Neha", "Amit", "Priya", "Kiran", "Meena", "Arjun"]
marks = [35, 75, 40, 90, 55, 30, 88]

# 1. List comprehension → Students who passed (marks > 40)
passed_marks = [m for m in marks if m > 40]
print("Marks of passed students:", passed_marks)

# 2. Dictionary comprehension → {student_name: grade}
grades = {
    student: ("A" if mark >= 75 else
              "B" if mark >= 60 else
              "C" if mark >= 40 else
              "F")
    for student, mark in zip(students, marks)
}
print("\nStudent Grades:", grades)

# 3. Set comprehension → Unique grades
unique_grades = {grade for grade in grades.values()}
print("\nUnique Grades:", unique_grades)

# 4. Tuple comprehension (actually generator expression) → Squares of marks
squares_gen = (m**2 for m in marks)   # generator expression
squares_tuple = tuple(squares_gen)    # converting to tuple
print("\nSquares of Marks (Tuple):", squares_tuple)
