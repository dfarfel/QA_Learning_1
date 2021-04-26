class Student:
    def __init__(self):
        self.id = 0
        self.student_name = None
        self.grade = 0
    def checkPass(self):
        if self.grade>=70:
            passed=True
        else:
            passed=False
        return passed
    def updateGrade(self,procent):
        if type(procent) == int:
            self.grade += (self.grade*procent)/100
            if self.grade > 100:
                self.grade = 100
        else:
            print("Should be int")
        return self.grade
    def print_(self):
        print(f"Name of student - {self.student_name}\nId of student - {self.id}\nStudent's grade - {self.grade}")