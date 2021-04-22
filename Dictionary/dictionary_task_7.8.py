list_names=["yosi","david","rachel","moshe","avraam"]
list_grades=[100,50,57,20,89]
list_over_avarage=[]
my_dict={}
index=0
for name in list_names:
    my_dict[name]=list_grades[index]
    index+=1
avarage_grade=sum(list_grades)/index
for name in my_dict:
    if my_dict[name]>=avarage_grade:
        list_over_avarage.append(name)
print(list_over_avarage)
