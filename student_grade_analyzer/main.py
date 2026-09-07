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



def run_program():

    analyzer = StudentGradeAnalyzer()
    analyzer.initial_record()

    while True:


            print("""
    Welcome to Student Grade Analyzer V2.0!
    1. All students (10 students)
    2. All grades
    3. Highest grade
    4. Lowest grade
    5. Average grade
    6. Passing students
    7. Failing students
    8. Students with Honors
    9. Search Student Enrollment ('in')
    10. Verify Memory Identity (copy, id, is, ==)
    11. Adding a student record 
""")
            choices = input("\nEnter your choices from 1 to 11: ")

            if choices == "1":
                   display_students_table(analyzer.students)

            elif choices == "2":
                grades = analyzer.get_all_grades()
                print("\nGrades:")
                print(*(f"{i}. {g}" for i, g in enumerate(grades, start=1)), sep="\n")

            elif choices == "3":
                 highest = analyzer.get_highest_grade()
                 print(f"\nHighest Grade: {highest}")
               
            
            elif choices == "4":
                 lowest = analyzer.get_lowest_grade()
                 print(f"\nLowest Grade: {lowest}")
                 pass
            
            elif choices == "5":
                 average = analyzer.calculate_average()
                 print(f"\nAverage Grade: {average}")
                 pass
            
            elif choices == "6":
                 passing_grade = analyzer.get_passing_students()
                 print("\nList of Passed Students:")
                 print(*(f"{i}. {g}" for i, g in enumerate(passing_grade, start=1)), sep="\n")

            elif choices == "7":
                 print("\nList of Failing Students:")
                 failing_students = analyzer.get_failing_students()
                 print(*(f"{i}. {g}" for i, g in enumerate(failing_students, start=1)), sep="\n")
                 
            elif choices == "8":
                honor_students = analyzer.get_honors_students()
                print("\nList of Honor Students:")
                print(*(f"{i}. {g}" for i, g in enumerate(honor_students, start=1)), sep="\n")

            elif choices == "9":

                 ask_student_name = input("Enter student name to find: ").capitalize()
                 print(f"Is {ask_student_name} enrolled student: {analyzer.is_enrolled(ask_student_name)}")

            elif choices == "10":
                 mem = analyzer.get_memory()
                 print("\n--- Memory Verification ---")
                 print(f"Original ID      : {mem['orig_id']}")
                 print(f"Copy ID          : {mem['copy_id']}")
                 print(f"Values Equal (==): {mem['is_equal']}")
                 print(f"Same Object (is) : {mem['is_same_object']}")

            elif choices == "11":
                 name = input("\nEnter student name: ").strip()
                 while True:
                      try:
                          grade = float(input("Enter grade (0-100): ").strip())
                          if 0 <= grade <= 100:
                            break
                          print("Grade must be between 0 and 100.")
                      except ValueError:
                       print("Please enter a valid numeric grade.")
                 analyzer.add_student_record(name, grade)
                 print(f"Successfully added {name} ({grade:.2f})!")

            elif choices == "0":
                print("Goodbye")
                break

            else:
                 return "invalid input"



run_program()