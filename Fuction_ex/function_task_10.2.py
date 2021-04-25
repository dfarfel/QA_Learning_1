import random
def sum_list(list1):
    return sum(list1)
list1=[]
for i in range(10):
    num=random.randint(1,9)
    list1.append(num)
print(list1)
print(multi_list(list1))
