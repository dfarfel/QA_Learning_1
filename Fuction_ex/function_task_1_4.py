def sum_till_num(num):
    sum_1=0
    for i in range(1,num+1):
        sum_1+=i
    return sum_1

user_num=int(input("Enter number: "))
print(sum_till_num(user_num))