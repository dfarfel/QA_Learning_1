num=str(input("Enter your number: "))
sum=0
for i in num:
    if i.isdigit():
        sum+=int(i)
print(f'the sum of digits in your number is: {sum}')


