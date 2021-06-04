
class Course:
    def __init__(self,number,name,max_students=30):
        self.number = number
        self.name = name
        self.subject_dict = {}
        self.student_list = []
        self.max_students=max_students

    def __repr__(self):
        return f'Number of a course - {self.number}. Name - {self.name}. Subjects - {self.subject_dict}. ' \
               f'Students - {self.student_list}. Capacity - {self.max_students} students'

    def check_space(self):
        if len(self.student_list) < self.max_students:
            return True
        else:
            return False

    def add_student(self,student):
        if self.check_space():
            self.student_list.append(student)

    def add_factor(self,subject,percent):
        try:
            for student in self.student_list:
                student.calc_factor(subject,percent)
        except:
            print("Something wrong")
            self.add_factor(subject, percent)

    def del_student(self,id):
        try:
            index=self.student_list.index(id)
            del self.student_list[index]
            return self.student_list
        except:
            print("Something wrong")
            self.del_student(id)

