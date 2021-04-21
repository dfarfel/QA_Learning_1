num1=int(input("Please enter number 1: "))
num2=int(input("Please enter number 2: "))
while num2%2==0 and num1%2==0:
    print(f'{num1+num2}')
    num1 = int(input("Please enter number 1: "))
    num2 = int(input("Please enter number 2: "))
print(f'{num1*num2}')
