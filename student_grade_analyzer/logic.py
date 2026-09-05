# ============================================================
# CMPE 201 Section2-2 - Data Structures and Algorithm
# FINAL CHALLENGE: Student Grade Analyzer
# Submitted by GROUP 5
# Ferrer, Angelo Terrence D.
# Flores, Prince Menard T.
# Guillen, Rod John F.
# Mayor, John Luis V.
# Pagdanganan, Kryzle Camille S.
# ============================================================

def display_students(students):
    """Displays all students with their assigned index and grade."""
    pass

def calculate_average(grades):
    """Calculates the numerical average (mean) of grades."""
    pass

def get_passing_students(students):
    """Filters and retrieves all students who achieved a passing grade."""
    pass

def get_failing_students(students):
    """Filters and retrieves all students whose grades fall below the passing threshold."""
    pass

def add_new_student_record(students):

    ask_name = input("Enter the name of the student: ").strip

    while True:
        ask_grade = int(input("Enter grade of the student: ")).strip

        try:
            grade = float(ask_grade).strip
        except ValueError:
            print("Incorrect value, enter a number!")

    new_record = (ask_name, grade)
    student_data.append(new_record)
    print(f"Successfully added {name} with a grade of {grade:.2f}!")


#student data

student_data = [
    ("Kryzle", 92.5),
    ("Mark", 68.0),
    ("Rod", 85.5),
    ("Diana", 94.0),
    ("Evan", 72.0),
    ("Fiona", 88.0),
    ("George", 55.5),
    ("Hannah", 91.0),
    ("Ian", 79.5),
    ("Prince", 64.0)
]
