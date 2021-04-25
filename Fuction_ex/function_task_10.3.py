import random
def multip_list(list_a):
    mult=1
    for i in list_a:
        mult=mult*i
    return mult
list1=[]
for i in range(5):
    num=random.randint(-10,10)
    list1.append(num)
print(multip_list(list1))