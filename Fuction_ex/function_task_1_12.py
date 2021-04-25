import random
def fill_list_2(l1):
    for i in range(20):
        ran_num=random.randint(1,100)
        l1.append(ran_num)
    return l1
def list_repeats(list_1,num_1):
    for i in range(num_1):
        print(list_1)

# list_1=[]
# print(fill_list_2(list_1))
# user_num=int(input("Enter quantity of repeats: "))
# list_repeats(list_1,user_num)

