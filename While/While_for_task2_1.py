# # Check prime numbers program
while True:
    num=(input("Please enter your number: "))
    while int(num)!= 1 and (int(num)==2 or int(num)%2!=0):
        for dig in range(2,int(num)):
            if int(num)%dig==0:
                print(f'Number {num} is not prime')
                num = (input("Please enter your number: "))
        print(f'Number {num} is prime')
        num = (input("Please enter your number: "))
    print(f'Number {num} is not prime')




