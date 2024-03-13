class Grader:
    def __init__(self, grades: list[list[float]]):
        self.grades = grades
 
    def compute(self):
        return [self.transform_raw(self.compute_student(student))
                for student in self.grades]
 
    def compute_student(self, student_grades: list[float]):
        return sum(student_grades) / len(student_grades)
 
    def transform_raw(self, raw: float):
        if raw < 60:
            return '5.00'
        elif 60 <= raw < 65:
            return '3.00'
        elif 65 <= raw < 70:
            return '2.75'
        elif 70 <= raw < 75:
            return '2.50'
        elif 75 <= raw < 80:
            return '2.25'
        elif 80 <= raw < 84:
            return '2.00'
        elif 84 <= raw < 88:
            return '1.75'
        elif 88 <= raw < 92:
            return '1.50'
        elif 92 <= raw < 96:
            return '1.25'
        elif 96 <= raw:
            return '1.00'
        
# 1
class MinGrader(Grader):
    def compute_student(self, student_grades: list[float]):
        for x in range(len(student_grades)):
            if student_grades[x] < 50:
                student_grades[x] = 50
        print(student_grades)

        return sum(student_grades) / len(student_grades)

# 2
class ExtremistGrader(Grader):
    def transform_raw(self, raw: float):
        if raw >= 99:
            return '1.00' 
        elif 60 <= raw < 99:
            return '3.00'
        else:
            return '5.00'

# 3
class StepUpGrader(Grader):
    def __init__(self, n: int, grades: list[list[float]]):
        super().__init__(grades)
        self.n = n
        
    def stepup(self):
        raw_list = self.compute()

        grades_list = ['5.00', '3.00', '2.75', '2.50', '2.00', '1.75', '1.50', '1.25', '1.00']
        
        raw_index = 0

        for raw in raw_list:
            if raw != '5.00' and raw != '1.00' and self.n >= 1 and raw:
                try:
                    index = grades_list.index(raw)
                    raw = grades_list[index + self.n]
                    
                except Exception:
                    raw = '1.00'

            raw_list[raw_index] = raw
            raw_index += 1

        return raw_list
        
                
grades: list[list[float]] = [[100, 100, 100, 99], [60, 60, 60, 60], [30, 50, 100, 20], [0, 0, 0, 0]]

x = MinGrader(grades)
print(x.compute())

y = ExtremistGrader(grades)
print('extreme', y.compute())

z = StepUpGrader(1, grades)
print('step', z.stepup())