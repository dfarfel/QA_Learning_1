class Course:
    def __init__(self):
        self.course_num=0
        self.name_course=None
        self.num_students=0
        self.max_num_students=50
    def info(self):
        info_=(f'Course number is {self.course_num}. Name of a course is {self.name_course}. Number of students at this course is {self.num_students}. Maximum capacity of students is {self.max_num_students}')
        return info_
    def vacancy(self):
        vacancy_=self.max_num_students-self.num_students
        return vacancy_
qa=Course()