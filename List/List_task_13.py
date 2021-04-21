import random
while True:
    list1=[]
    for i in range(20):
        rand_num=random.randrange(1,100)
        list1.append(rand_num)
    print(list1)
    user_num=int(input("Enter the number that will be removed: "))
    list2=list1
    for i in range(list1.count(user_num)):
        list2.remove(user_num)
    print(list2)
    print("One more time")