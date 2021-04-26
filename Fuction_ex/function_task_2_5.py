def list_d(str_dict_set_tuple):
    list_1=[]
    if type(str_dict_set_tuple)==str or type(str_dict_set_tuple)==dict or type(str_dict_set_tuple)==set or type(str_dict_set_tuple)==tuple:
        for i in str_dict_set_tuple:
            list_1.append(i)
    else:
        print("None\nError")
    return list_1
