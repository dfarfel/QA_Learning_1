import random
list1=[]
for i in range(10):
    rand_num=random.randint(1,101)
    list1.append(rand_num)
user_num=int(input("Enter your number: "))
list1.append(user_num)
tuple1=tuple(list1)
list1=list(tuple1[0:4])
tuple2=tuple1[-1:-5:-1]
list1.append(tuple2)
tuple1=list1
list1=list(tuple1)
del list1[0]
tuple1=tuple(list1)
print(tuple1)

