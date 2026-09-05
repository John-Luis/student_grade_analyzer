"""
CMPE 201 - Final Challenge: Student Grade Analyzer
Group 5 Collaboration Project
File: main.py (User Interface & Menu Loop)
"""

from logic import StudentGradeAnalyzer

def display_students_table(students_list):
    """Displays all 10 students with clean tabular formatting."""
    print(f"\n{'No.':<4} {'Name':<15} {'Grade':<6}")
    print("-" * 28)
    for i in range(len(students_list)):
        name, grade = students_list[i]
        print(f"{i + 1:<4} {name:<15} {grade:<6.2f}")

def testing():
    analyzer = StudentGradeAnalyzer()
    analyzer.initial_record()
    display_students_table(analyzer.students)

testing()

def run_program():

    while True:
            analyzer = StudentGradeAnalyzer()
            analyzer.initial_record()

            print("""
    Welcome to Student Grade Analyzer V2.0!
    1. All students (10 students)
    2. All grades
    3. Highest grade
    4. Lowest grade
    5. Average grade
    6. Passing students
    7. Failing students
    8. Students with grades above 90
    9. Adding a student record
""")
            choices = input("Enter your choices from 1 to 9:")

run_program()