from Class_object.Class_task_2 import Student
student_1=Student()
student_1.student_name="Moshe"
student_1.grade=60
student_1.id=333333
if student_1.check_pass():
    print("Passed")
else:
    print("Failed")
student_1.update_grade(50)
student_1.print_()