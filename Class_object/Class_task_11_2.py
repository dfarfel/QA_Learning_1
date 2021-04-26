class StudentInClass:
    def __init__(self):
        self.id = 0
        self.student_name = None
        self.address = None
        self.grade = 0
    def passed_grade(self):
        if self.grade>=70:
            passed=True
        else:
            passed=False
        return passed
