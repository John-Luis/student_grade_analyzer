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
import pandas as pd
import numpy as np

class StudentGradeAnalyzer:

    # DO NOT CHANGE
    def __init__(self):
        self.students = []

    def initial_record(self):

        initial_records = [
            ("Kryzle", 92.5),
            ("Prince", 68.0),
            ("Clark", 85.5),
            ("Diane", 94.0),
            ("Francis", 72.0),
            ("Allen", 88.0),
            ("Duke", 55.5),
            ("Justine", 91.0),
            ("Jake", 79.5),
            ("Rod", 64.0)
        ]
        for record in initial_records:
            self.students.append(record)


    def add_student_record(self, name, grade):
        self.students.append((name, float(grade)))
    # 
    # ==============================================================================
    # EXTRACTION BASIS
    # How this list comprehension works:
    #   [ <output_expression> for <variables> in <iterable> ]
    #
    # 1. <iterable>: self.students (the list of tuples)
    # 2. for _, grade in self.students:
    #      - It unpacks each 2-element tuple: (name, grade).
    #      - We use '_' as an underscore variable because we don't need the name here.
    #      - 'grade' captures the numerical value (e.g., 92.5, 68.0).
    # 3. <output_expression>: grade (at the front)
    #      - Tells Python to place ONLY the numerical grade into the new list.
    # ==============================================================================

    def get_all_grades(self):
        """List Comprehension: Extracts all numerical grades from the student records."""
        return [grade for _, grade in self.students]



    # DO NOT CHANGE
    # ==============================================================================================================================
    # TASK OF ANGELO AND ROD (Tasks 3, 4, 5)
    # WHAT DATA TO USE:
    #   Call 'self.get_all_grades()' to get a clean list of numbers:
    #   e.g., [92.5, 68.0, 85.5, 94.0, ...]
    # PYTHON CONCEPTS TO USE:
    #   - max(list_of_numbers) -> returns the highest score
    #   - min(list_of_numbers) -> returns the lowest score
    #   - sum(list_of_numbers) / len(list_of_numbers) -> calculates class average
    # ==============================================================================================================================

    def validate(self, grades):
        """Validates grades list and returns a Pandas Series."""
        if grades is None:
            grades = self.get_all_grades()

        for grade in grades:
            if grade < 0 or grade > 100:
                return pd.Series([np.nan])

        return pd.Series(grades)

    def get_highest_grade(self):
        grades_series = self.validate()
        return grades_series.dropna().max()

    def get_lowest_grade(self):
        pass

    def calculate_average(self):
        pass

    # ==============================================================================
    # TASK OF MENARD AND KRYZLE (Tasks 6, 7, 8)    
    # # Dito, the data or "ITERATION" that you will use is the self.student.
    # HOW TUPLE UNPACKING WORKS HERE:
    #   Write: for name, grade in self.students
    #     - 'name'  receives Position 0 of the tuple (e.g., "Kryzle")
    #     - 'grade' receives Position 1 of the tuple (e.g., 92.5)
    #
    # COMPREHENSION STRUCTURE WITH FILTER:
    #   [ name for name, grade in self.students if <condition_on_grade> ]
    #
    #   - Output Expression = 'name' (you want a list of student names)
    #   - Variables         = 'name, grade' (unpacks both elements)
    #   - Iterable          = 'self.students'
    #   - Condition         = checks 'grade' against the benchmark
    # ==============================================================================
    
    def get_passing_students(self, passing_grade = 75.0):
        """List Comprehension: Returns names of students with passing grades (>= 75.0)."""
        return [name for name, grade in self.students if grade >= passing_grade]

    def get_failing_students(self, failing_grade = 75.0):
        """List Comprehension: Returns names of students with failing grades (< 75.0)."""
        return [name for name, grade in self.students if grade < failing_grade]

    def get_honors_students(self, honors_grade = 90.0):   
        """List Comprehension: Returns names of students with grades above 90.0."""
        return [name for name, grade in self.students if grade > honors_grade]


    # ========================================================================================
        # DO NOT CHANGE

    def get_memory(self):
        students_copy = self.students.copy()
        return {
            "orig_id": id(self.students),
            "copy_id": id(students_copy),
            "is_equal": students_copy == self.students,
            "is_same_object": students_copy is self.students
        }

    def is_enrolled(self, target_name):
        names = [name for name, _ in self.students]
        return target_name in names





