from Class_object.Concluding_task_1 import Student
from Class_object.Concluding_task_2 import Course
user_num=int(input("Enter a number of the course:  "))
user_name_course=input("Enter a name of the course: ")
user_num_subject=int(input("Enter the number of subjects: "))
user_capacity=int(input("Enter a max number of students: "))
user_student_list=[]

user_subject_dict={}
for i in range(user_num_subject):
    user_teacher=input("Enter a name of teacher: ")
    user_subject=input("Enter a name of subject:")
    user_subject_dict.update({user_teacher:user_subject})

course_1 = Course(user_num, user_name_course,user_capacity)

user_id=int(input("Enter the id of student.If '0' - End of input:  "))
while user_id != 0:
    if not course_1.check_space():
        print("There is no place")
        break

    user_student_name=input("Enter the name of student: ")

    user_grade_dict = {}
    for i in range(int(input("Enter the number of subjects: "))):
        user_student_subject = input("Enter the name of subject: ")
        user_grade=int(input("Enter the grade: "))
        user_grade_dict.update({user_student_subject:user_grade})

    student_1=Student(user_id,user_grade_dict,user_student_name)

    course_1.add_student(student_1)
    print(course_1)

    user_id = int(input("Enter the id of student.If '0' - End of input:  "))

user_factor_subject=input("Enter the name of subject you gonna do factor: ")
user_num_factor=float(input("Enter the percent you want: "))
course_1.add_factor(user_factor_subject, user_num_factor)
print(course_1)

min=100

for studen in course_1.student_list:
    avarage=studen.avarage()
    if avarage<min:
        min=avarage

for stud in course_1.student_list:
    if stud.avarage()==min:
        course_1.del_student(stud)


print(course_1)
