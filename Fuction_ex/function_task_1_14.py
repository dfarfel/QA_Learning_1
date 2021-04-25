def list_student_grade(num_1):
    list1 = []
    for i in range(num_1):
        grade = int(input("Enter the grade: "))
        list1.append(grade)
    return list1

# user_num = int(input("Enter the number of students: "))
# print(list_student_grade(user_num))