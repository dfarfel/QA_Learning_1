my_dict={1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 25,11:4}
my_dict_2=my_dict.copy()
list_values=list(my_dict_2.values())
double_value=0
for value in list_values:
    if list_values.count(value)>1:
        double_value=value
        for key in my_dict:
            value_my_dict=my_dict[key]
            if double_value==value_my_dict:
                my_dict_2.pop(key)
                list_values = list(my_dict_2.values())
                break
print(my_dict_2)
