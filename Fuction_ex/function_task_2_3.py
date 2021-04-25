def find_d(list_d,object_d,start):
    index=start
    for i in list_d[start::]:
        if i==object_d:
            break
        else:
            index += 1
    return index