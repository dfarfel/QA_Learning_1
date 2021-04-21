grade=input("Please enter the grade: ")
count=0
num=1
avarage_pass=0
avarage_fail=0
while 100>=int(grade) and int(grade)>=0:
    grade = int(grade)
    if grade>60:
        print("passed")
        count+=grade
        avarage_pass=count/num
        num += 1
        grade = input("Please enter the grade: ")

    else:
        print("Failed")
        grade = input("Please enter the grade: ")
print("The grade is invalid")

