num1=int(input("Please enter number: "))
if 99<num1<1000:
    print(f'{(num1//100)+(num1//10%10)+(num1%10)}')
else:
    print("ERROR!")
    print("Hello Git!")