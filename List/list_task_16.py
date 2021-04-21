str1=input("Enter your list with comma: ")
list1=(str1.split(","))
list2=[]
for i in list1:
    list2.append(i)
    if list1.count(i)>1:
        list2.remove(i)
print(list2)