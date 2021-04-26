from Class_object.Class_task_11_2 import StudentInClass
student_1=StudentInClass()
student_1.student_name="Dani"
student_1.address="Yafo Tel-Aviv"
student_1.id=33333
student_1.grade=80


if student_1.passed_grade():
    print("Passed")
else:
    print("Failed")
