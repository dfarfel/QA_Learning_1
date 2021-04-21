#dividing of float number without % and //
num_1=int(input("Enter first number: "))
num_2=int(input("Enter second number: "))
if num_1>num_2:
    divide_num=num_1/num_2
    print(f'Dividing dose is {int(divide_num)}')
    print(f'Rest is {num_1-num_2*int(divide_num)}')
else:
    print("First number must be bigger than second")

