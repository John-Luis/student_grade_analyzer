# Student Grade Analyzer

---

## Developers
* **Ferrer, Angelo Terrence D.**
* **Flores, Prince Menard T.**
* **Guillen, Rod John F.**
* **Mayor, John Luis V.**
* **Pagdanganan, Kryzle Camille S.**

---

## Project Overview
The **Student Grade Analyzer** is a Python CLI application designed to record, process, and analyze student academic marks. Built for the CMPE 201 Final Challenge, the application demonstrates key Python data structures, list operations, memory diagnostics, and statistical analysis using Pandas and NumPy.

---

## Key Features & Core Concepts

### Academic Analytics
* **Roster Management:** View all baseline student records in a clean tabular view or add new custom entries dynamically.
* **Statistical Insights:** Computes highest, lowest, and class average grades safely with missing-value (`NaN`) handling.
* **Filtered Lists:** Categorizes student names into Passing (>=75.0), Failing (<75.0), and Honors (>90.0) using Python list comprehensions.

### Technical Demonstrations
* **List Comprehensions:** Concise list creation and conditional filtering across 4 separate functions.
* **Tuple Unpacking:** Extracting names and numerical scores from tuple entries `(name, grade)`.
* **Membership Testing:** Checking active enrollment status using the `in` operator.
* **Memory Diagnostics:** Verifying object identity and value equality (`id()`, `is`, `==`, and `.copy()`).

---

## Project Structure

```text
student_grade_analyzer/
│
└── student_grade_analyzer/
    ├── logic.py      # StudentGradeAnalyzer class containing data structures & methods
    └── main.py       # Interactive CLI user interface menu
