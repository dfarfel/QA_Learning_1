def sum_3_digit(num):
    sum1=0
    for digit in str(num):
        sum1+=int(digit)
    return sum1

user_num=input("Enter a 3-digit number: ")
if 100<=int(user_num)<=999:
    print(f'The sum of digit is {sum_3_digit(user_num)}')
else:
    print("Your number is not 3-digit")
