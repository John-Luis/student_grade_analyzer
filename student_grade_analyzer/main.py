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
