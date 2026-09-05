import pandas as pd
import numpy as np

class GradeStatistics:
    
    def validate(self, grades):

        for grade in grades:
            
            if grade < 0 or grade > 100:
                return np.nan
    
        valid_grades =  [
            75 if grade < 75 and grade > 0 else grade
            for grade in grades
        ]
        
        return valid_grades
    
    def highes(self, grades):
        grades = self.validate(grades).dropna()
        
        return grades.max()
    
    def lowest(self, grades):
        pass
    
    def average(self, grades):
        pass