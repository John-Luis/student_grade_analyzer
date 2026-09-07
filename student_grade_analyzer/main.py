"""
CMPE 201 - Final Challenge: Student Grade Analyzer
Group 5 Collaboration Project
Section: 2-2
Members:
- Ferrer, Angelo Terrence D.
- Flores, Prince Menard T.
- Guillen, Rod John F.
- Mayor, John Luis V.
- Pagdanganan, Kryzle Camille S.

File: main.py (User Interface & Menu Loop)
"""

import time
from logic import StudentGradeAnalyzer


def pause_screen():
    """Pauses the output so the user can review results before returning to menu."""
    time.sleep(0.3)
    input("\n[Press Enter to return to the Main Menu...]")


def display_students_table(students_list):
    """Displays all students with clean tabular formatting."""
    print(f"\n{'No.':<4} {'Name':<15} {'Grade':<6}")
    print("-" * 28)
    for i in range(len(students_list)):
        name, grade = students_list[i]
        print(f"{i + 1:<4} {name:<15} {grade:<6.2f}")


def run_program():
    # Application startup header
    print("=" * 60)
    print("      CMPE 201 - DATA STRUCTURES AND ALGORITHMS")
    print("             FINAL CHALLENGE: GROUP 5")
    print("=" * 60)
    print("Welcome to the Student Grade Analyzer System!")
    print("Initializing baseline records...")
    time.sleep(0.8)

    analyzer = StudentGradeAnalyzer()
    analyzer.initial_record()
    print("Ready!\n")
    time.sleep(0.4)

    while True:
        print("\n" + "=" * 50)
        print("          STUDENT GRADE ANALYZER V2.0")
        print("=" * 50)
        print(" 1. All students (10 students)")
        print(" 2. All grades")
        print(" 3. Highest grade")
        print(" 4. Lowest grade")
        print(" 5. Average grade")
        print(" 6. Passing students")
        print(" 7. Failing students")
        print(" 8. Students with Honors")
        print(" 9. Search Student Enrollment ('in')")
        print(" 10. Verify Memory Identity (copy, id, is, ==)")
        print(" 11. Add a student record")
        print("  0. Exit Application")
        print("=" * 50)

        choices = input("Enter your choice (0-11): ").strip()

        if choices == "1":
            print("\n--- Current Class Roster ---")
            display_students_table(analyzer.students)
            pause_screen()

        elif choices == "2":
            grades = analyzer.get_all_grades()
            print("\n--- All Numerical Grades ---")
            if grades:
                print(*(f"{i}. {g:.2f}" for i, g in enumerate(grades, start=1)), sep="\n")
            else:
                print("No grades recorded.")
            pause_screen()

        elif choices == "3":
            highest = analyzer.get_highest_grade()
            print(f"\n--- Statistic ---\nHighest Grade: {highest}")
            pause_screen()

        elif choices == "4":
            lowest = analyzer.get_lowest_grade()
            print(f"\n--- Statistic ---\nLowest Grade: {lowest}")
            pause_screen()

        elif choices == "5":
            average = analyzer.calculate_average()
            print(f"\n--- Statistic ---\nClass Average: {average:.2f}")
            pause_screen()

        elif choices == "6":
            passing_students = analyzer.get_passing_students()
            print("\n--- List of Passing Students (>= 75) ---")
            if passing_students:
                print(*(f"{i}. {name}" for i, name in enumerate(passing_students, start=1)), sep="\n")
            else:
                print("No students passed.")
            pause_screen()

        elif choices == "7":
            failing_students = analyzer.get_failing_students()
            print("\n--- List of Failing Students (< 75) ---")
            if failing_students:
                print(*(f"{i}. {name}" for i, name in enumerate(failing_students, start=1)), sep="\n")
            else:
                print("No failing students.")
            pause_screen()

        elif choices == "8":
            honor_students = analyzer.get_honors_students()
            print("\n--- List of Honor Students (> 90) ---")
            if honor_students:
                print(*(f"{i}. {name}" for i, name in enumerate(honor_students, start=1)), sep="\n")
            else:
                print("No students qualified for honors.")
            pause_screen()

        elif choices == "9":
            ask_student_name = input("\nEnter student name to find: ").strip().capitalize()
            enrolled = analyzer.is_enrolled(ask_student_name)
            status = "ENROLLED" if enrolled else "NOT ENROLLED"
            print(f"Result: {ask_student_name} is {status} in the class record.")
            pause_screen()

        elif choices == "10":
            # Matches logic.py method name: get_memory_diagnostics
            mem = analyzer.get_memory()
            print("\n--- Memory Verification Diagnostics ---")
            print(f"Original Object ID (self.students) : {mem['orig_id']}")
            print(f"Copy Object ID (.copy())           : {mem['copy_id']}")
            print(f"Value Equality check (==)          : {mem['is_equal']}")
            print(f"Reference Identity check (is)      : {mem['is_same_object']}")
            pause_screen()

        elif choices == "11":
            print("\n--- Add New Student Record ---")
            name = input("Enter student name: ").strip().capitalize()
            while True:
                try:
                    grade = float(input("Enter grade (0-100): ").strip())
                    if 0 <= grade <= 100:
                        break
                    print("Grade must be between 0 and 100.")
                except ValueError:
                    print("Invalid input. Please enter a numerical grade.")

            analyzer.add_student_record(name, grade)
            print(f"\nSuccess: Added {name} with a grade of {grade:.2f}!")
            pause_screen()

        elif choices == "0":
            print("\nThank you for using Student Grade Analyzer V2.0!")
            print("Exiting application...")
            time.sleep(0.5)
            break

        else:
            print("\n[!] Invalid selection. Please enter a number from 0 to 11.")
            time.sleep(0.8)


if __name__ == "__main__":
    run_program()