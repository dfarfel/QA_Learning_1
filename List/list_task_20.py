import random
list1=[]
user_index=0
index=0
for i in range(10):
    rand_num=random.randrange(1,10)
    list1.append(rand_num)
user_num=int(input("Enter your number: "))
if user_num in list1:
    for num in list1:
        if user_num==num:
            user_index=index
            break
        else:
            index+=1
    print(user_index)
else:
    print("The number is out of list")