def remove_d(list_d,object_d):
    list_1=[]
    count=0
    for i in list_d:
        if i!=object_d:
            list_1.append(i)
            count+=1
        else:
            for a in list_d[count+1::]:
                list_1.append(a)
            break



    return list_1