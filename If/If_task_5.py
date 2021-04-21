def convert():
    num1 = int(input("Please enter number: "))
    num2 = int(input("Please enter number: "))
    if num1%2==0 and num2%2==0:
        print(f'{num1+num2}')
    else:
        print(f'{num1*num2}')

convert()
while True:
    end_prog=input('One more? [1/0]: ')
    if end_prog == "1":
        convert()
    else:
        break