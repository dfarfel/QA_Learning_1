my_dict={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
dict_rev={}
list_values=list(my_dict.values())
index=0
for key in my_dict:
    dict_rev[list_values[index]]=key
    index+=1
print(dict_rev)
