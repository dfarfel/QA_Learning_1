def check_letter_up_or_low(str1):
    count_upp=0
    count_low=0
    for i in str1:
        if i.isupper():
            count_upp+=1
        elif i.islower():
            count_low+=1
    return count_low,count_upp

user_str=str(input("Enter your string: "))
print(f'Quantity of low letter is {check_letter_up_or_low(user_str)[0]}\nQuantity of upp letter is {check_letter_up_or_low(user_str)[1]}')
