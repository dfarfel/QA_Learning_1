def division_7_3(low,high):
    list_3=[]
    list_7=[]
    for i in range(int(low),int(high)+1):
        if i%3==0:
            list_3.append(str(i))
        if i%7==0:
            list_7.append(str(i))
    return list_3,list_7
