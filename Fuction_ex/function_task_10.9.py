def sum_even_number(list1):
    list2=[]
    for i in list1:
        if int(i)%2==0:
            list2.append(int(i))
    sum_1=sum(list2)
    return sum_1

user_list=str(input("Enter your list with comma:")).split(",")
print(sum_even_number(user_list))
