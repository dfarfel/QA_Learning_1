num=int(input("Enter number: "))
while 100<=num<=999:
    print(f'{num//100+num//10%10+num%10}')
    num = int(input("Enter number: "))
print("Error")
