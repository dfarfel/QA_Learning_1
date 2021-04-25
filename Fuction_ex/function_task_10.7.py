def remove_double_list(list1):
    list2=[]
    for i in list1:
        if i not in list2:
            list2.append(i)
        else:
            continue
    return list2
list_1=[10,204,30,10,435,4365,40,30,435]
print(remove_double_list(list_1))