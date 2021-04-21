num1=int(input("Please enter number: "))
num2=int(input("Please enter number: "))
if num1>num2:
    print(f'{num1-num2}')
else:
    if num1<num2:
        print(f'{num2-num1}')
    else:
        print(0)