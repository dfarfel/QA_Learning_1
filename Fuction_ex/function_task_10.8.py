import sys
def prime_check(num):
    while int(num) != 1 and (int(num) == 2 or int(num) % 2 != 0):
        if num==2:
            print(f'Number {num} is prime')
            sys.exit()
        for digit in range(2, int(num)):
            if int(num) % digit == 0:
                print(f'Number {num} is not prime')
                sys.exit()
        print(f'Number {num} is prime')
        sys.exit()
    print(f'Number {num} is not prime')

user_num=int(input("Enter your number: "))
prime_check(user_num)
