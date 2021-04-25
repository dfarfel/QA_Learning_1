from Fuction_ex.function_task_1_6 import print_num_in_range
def ret_bigger_num(num_1,num_2):
    list1=[num_1,num_2]
    return max(list1)
def ret_smaller_num(num_1,num_2):
    list_1=[num_1,num_2]
    return min(list_1)


user_num_1=int(input("Enter your number: "))
user_num_2=int(input("Enter your number: "))
print_num_in_range(ret_smaller_num(user_num_1,user_num_2),ret_bigger_num(user_num_1,user_num_2))