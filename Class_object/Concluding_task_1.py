class Student:
    def __init__(self,id,grades_dict = None,name=None):
        self.id=id
        self.name=name
        self.grades_dict=grades_dict

    def __eq__(self, other):
        if self.id == other:
            return True
        else:
            return False

    def __repr__(self):
        return f'Name - {self.name}. Id - {self.id}. Grades - {self.grades_dict}'

    def add_grade(self,subject,grade):
        try:
            self.grades_dict.update({subject:grade})
            return self.grades_dict
        except:
            print("Something wrong")
            self.add_grade(subject,grade)

    def calc_factor(self,subject,percent):
        try:
            grade_factor=self.grades_dict[subject] + ((self.grades_dict[subject] * percent)/100)
            if grade_factor > 100:
                grade_factor = 100
            self.grades_dict.update({subject:grade_factor})
            return self.grades_dict
        except:
            print("Something wrong")
            self.calc_factor(subject,percent)

    def avarage(self):
        try:
            avarage=sum(list(self.grades_dict.values())) / len(list(self.grades_dict.values()))
            return avarage
        except:
            print("Something wrong")
            self.avarage()