def is_3_digit(num):
    while num.isnumeric():
        if 100 <= int(num) <= 999:
            digit=True
        else:
            digit=False
        return digit


user_num=input("Enter a 3-digit number: ")
if is_3_digit(user_num):
    print(f'The number is a 3-digit')
else:
    print("Your number is not 3-digit")