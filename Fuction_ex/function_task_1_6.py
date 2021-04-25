def print_num_in_range(num_1,num_2):
    for i in range(num_1,num_2+1):
        print(i,end=" ")

user_num_1=int(input("Enter your number: "))
user_num_2=int(input("Enter your number: "))
print_num_in_range(user_num_1,user_num_2)