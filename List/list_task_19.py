import random
list1=[]
for i in range(10):
    random_num=random.randrange(1,100)
    list1.append(random_num)
print(list1)
for member in list1:
    print(f'Number {member} is appear {list1.count(member)} times')