import sys
list1=input("Enter the list of grades with cooma: ")
list1=list(map(float,list1.split(",")))
count_pass=0
count_fail=0
for i in list1:
    if 0>i or i>100:
        sys.exit("The grade is not correct please enter grades between 0 and 100")
    elif i>=60:
        count_pass+=1
    else:
        count_fail+=1

print(f'Quantity of passed grades - {count_pass}\nQuantity of failed grades - {count_fail}')

