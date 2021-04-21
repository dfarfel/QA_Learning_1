grade=int(input("Pleasse enter grade: "))
grade_1=0
count=0
sum=0
while 0<=grade and grade<=100:
    if grade_1<grade:
        grade_1=grade
    count+=1
    sum+=grade
    avarage=sum/count
    difference=grade_1-avarage
    grade = int(input("Please enter grade: "))
print(f'The biggest grade is {grade_1}\nThe avarage grade is {avarage}\nThe difference between the biggest grade and the avarage is {difference}')

    #print(grade_1)
