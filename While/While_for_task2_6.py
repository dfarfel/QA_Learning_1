# Reverse the number and double it
while True:
    num=input("Enter number: ")
    if num.isnumeric():
        sum_digit=0
        reverse_num=""
        for digit in num:
            sum_digit+=1
            for i in str(sum_digit):
                num_1=int(num)//(10**(sum_digit-1))%10
                reverse_num=str(reverse_num)+str(num_1)
        print(f'{reverse_num},{int(reverse_num)*2}')
    else:
        print("Number can be only positive")