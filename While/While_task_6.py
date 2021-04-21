grade=int(input("Pleasse enter the grade: "))
count_pass=0
count_fail=0
sum_pass=0
sum_fail=0
avarage_pass=0
avarage_fail=0
while 0<=grade<=100:
    if 70<=grade<=100:
        print("Passed")
        count_pass+=1
        sum_pass+=grade
        avarage_pass=sum_pass/count_pass
        grade = int(input("Pleasse enter the grade: "))
    else:
        print("Failed")
        count_fail+=1
        sum_fail+=grade
        avarage_fail=sum_fail/count_fail
        grade = int(input("Pleasse enter the grade: "))
print(f'Failed avarage = {avarage_fail}''\n'f'Passed avarage = {avarage_pass}')
