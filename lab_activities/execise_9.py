"""
CMPE 201: Final Challenge - Student Grade Analyzer
Group 5 Collaboration Project
"""

# ==========================================
# FUNCTION DEFINITIONS
# ==========================================

def display_students(student_records):
    """Displays all student records cleanly without raw index labels."""
    print("\nName                 Grade")
    print("-" * 30)
    for name, grade in student_records:
        print(f"{name:<20} {grade:<6.2f}")


def calculate_average(grade_list):
    """Calculates class average using sum() and len()."""
    if len(grade_list) == 0:
        return 0.0
    return sum(grade_list) / len(grade_list)


def get_passing_students(student_records):
    """List Comprehension #1: Filters passing students (grade >= 75)."""
    return [name for name, grade in student_records if grade >= 75]


def get_failing_students(student_records):
    """List Comprehension #2: Filters failing students (grade < 75)."""
    return [name for name, grade in student_records if grade < 75]

def add_new_student(student_records):
    """Prompts the user for a student name and grade, then appends a new tuple."""
    name = input("\nEnter student name: ").strip()
    
    # Simple validation to ensure valid numeric input
    while True:
        grade_input = input("Enter student grade (0 - 100): ").strip()
        try:
            grade = float(grade_input)
            if 0 <= grade <= 100:
                break
            print("Grade must be between 0 and 100.")
        except ValueError:
            print("Invalid number. Please enter a valid grade.")

    # Create the new tuple and append it to the mutable list
    new_record = (name, grade)
    student_records.append(new_record)
    print(f"Successfully added {name} with a grade of {grade:.2f}!")



# ==========================================
# DATA SETUP
# ==========================================

students = []

# Populate 10 student records using append()
student_data = [
    ("Alice", 92.5),
    ("Bob", 68.0),
    ("Charlie", 85.5),
    ("Diana", 94.0),
    ("Evan", 72.0),
    ("Fiona", 88.0),
    ("George", 55.5),
    ("Hannah", 91.0),
    ("Ian", 79.5),
    ("Jack", 64.0)
]

for record in student_data:
    students.append(record)

# List Comprehension #3: Extract all grades
grades = [grade for name, grade in students]

# List Comprehension #4: Filter honors students (grade > 90)
honors_students = [name for name, grade in students if grade > 90]


# ==========================================
# INTERACTIVE MENU SYSTEM
# ==========================================

def main_menu():
    while True:
        print("\n" + "=" * 38)
        print("     STUDENT GRADE ANALYZER")
        print("=" * 38)
        print("[1] View All Students (10 Records)")
        print("[2] View All Grades")
        print("[3] View Highest, Lowest & Average")
        print("[4] View Passing Students (>= 75)")
        print("[5] View Failing Students (< 75)")
        print("[6] View Honors Students (> 90)")
        print("[7] Memory & Copy Verification")
        print("[8] Search Student Enrollment ('in')")
        print("[0] Exit")
        print("=" * 38)

        choice = input("Enter option (0-9): ").strip()

        if choice == "1":
            print("\n=== ALL ENROLLED STUDENTS ===")
            display_students(students)

        elif choice == "2":
            print("\n=== ALL EXTRACTED GRADES ===")
            print("Grades:", grades)
            print("Total count:", len(grades))

        elif choice == "3":
            # Using indexing for first and last record
            first_student = students[0]
            last_student = students[-1]

            print("\n=== GRADE SUMMARY ===")
            print(f"Total Records: {len(students)}")
            print(f"First Entry:   {first_student[0]} ({first_student[1]:.2f})")
            print(f"Last Entry:    {last_student[0]} ({last_student[1]:.2f})")
            print("-" * 30)
            print(f"Highest Grade: {max(grades):.2f}")
            print(f"Lowest Grade:  {min(grades):.2f}")
            print(f"Average Grade: {calculate_average(grades):.2f}")

        elif choice == "4":
            passing = get_passing_students(students)
            print(f"\n=== PASSING STUDENTS ({len(passing)}) ===")
            print(passing)

        elif choice == "5":
            failing = get_failing_students(students)
            print(f"\n=== FAILING STUDENTS ({len(failing)}) ===")
            print(failing)

        elif choice == "6":
            print(f"\n=== HONORS STUDENTS (> 90) ({len(honors_students)}) ===")
            print(honors_students)

        elif choice == "7":
            # A copy of a list, ==, is, and id()
            students_backup = students.copy()
            print("\n=== REFERENCE & IDENTITY VERIFICATION ===")
            print("Original List ID:", id(students))
            print("Backup Copy ID:  ", id(students_backup))
            print("-" * 40)
            print("students == students_backup:", students == students_backup)
            print("students is students_backup:", students is students_backup)

        elif choice == "8":
            target = input("\nEnter student name to search: ").strip()
            names_only = [name for name, _ in students]
            is_enrolled = target in names_only
            print(f"Is '{target}' in the student list?: {is_enrolled}")

        elif choice == "9":
            add_new_student(students)
            # Crucial: update the grades and honors lists so the summary stays accurate!
            grades = [grade for name, grade in students]
            honors_students = [name for name, grade in students if grade > 90]

        elif choice == "0":
            print("\nExiting program. Goodbye!")
            break

        else:
            print("\nInvalid choice. Please select a number from 0 to 8.")


if __name__ == "__main__":
    main_menu()