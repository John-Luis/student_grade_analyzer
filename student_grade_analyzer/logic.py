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
        """Allows dynamically adding new student tuples."""
        self.students.append((name, float(grade)))


    # Here, ito na magiging basis niyo for data extraction. Mag puput na lang kayo ng for loop and filtering conditions. Hence, list comprehension.
    def get_all_grades(self):
        """List Comprehension: Extracts all numerical grades from the student records."""
        return [grade for _, grade in self.students]
    
    # DO NOT CHANGE
# ==============================================================================================================================

    # TASK OF ANGELO AND ROD. Pwede niyo na pagsamahin dito yung get highest and lowest function para mas maliit.
    def get_highest_grade(self):
        """3. Highest grade using max()."""
        # TODO: Angelo & Rod implement this
        pass

    def get_lowest_grade(self):
        """4. Lowest grade using min()."""
        # TODO: Angelo & Rod implement this
        pass

    def calculate_average(self):
        """5. Average grade using sum() and len()."""
        # TODO: Angelo & Rod implement this
        pass


    # TASK OF KRYZLE AND MENARD.. Tbh pwede niyo napagsamahin sa iisang function yung get passing sudent and failing student... only suggestion.

    
    def get_passing_students(self):
        """6. Passing students (grade >= 75) using list comprehension."""
        # TODO: Menard & Kryzle implement this
        pass

    def get_failing_students(self):
        """7. Failing students (grade < 75) using list comprehension."""
        # TODO: Menard & Kryzle implement this
        return [name for name, grade in self.students if grade >= 75 ]
        pass

    def get_honors_students(self):
        """8. Students with grades above 90 using list comprehension."""
        # TODO: Menard & Kryzle implement this
        pass


        # ========================================================================================
        # DO NOT CHANGE

    def get_memory_diagnostics(self):
        """Demonstrates copy(), id(), '==', and 'is' operators."""
        students_copy = self.students.copy()
        return {
            "orig_id": id(self.students),
            "copy_id": id(students_copy),
            "is_equal": students_copy == self.students,
            "is_same_object": students_copy is self.students
        }

    def is_enrolled(self, target_name):
        """Demonstrates membership checking using 'in'."""
        names = [name for name, _ in self.students]
        return target_name in names





