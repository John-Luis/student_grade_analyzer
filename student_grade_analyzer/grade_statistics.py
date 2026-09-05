class GradeStatistics:
    
    def validate(self, grades):
        valid_grades = []
        
        for grade in grades:
            
            if grade < 0 or grade > 100:
                return "Invalid Grade"
            
            if grade < 75 and grade > 0: 
                grade = 75 
            
            valid_grades.append(grade)
        
        return valid_grades
            