list1=[]
list4=[]
list5=[]
list6=[]
for i in range(1,11):
    list1.append(i)
for i in list1:
    list5.append(i * 2)
list6.append(list1[0])
list6.append(list1[-1])
list2=list1[-3:]
print(list2[-1:-4:-1])
print(list1[2::2])
list3=list1[1::2]
print(list3)
for i in range(3):
    num=int(input("Enter number: "))
    list4.append(num)
list1[4:6]=list4
list1.append(list1[2])
print(list1)
print(list5)
print(list6)
