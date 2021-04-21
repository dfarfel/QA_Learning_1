from random import randint
rand_num=randint(1,9)
num=int(input("Enter your number to guess program number: "))
while num!=rand_num:
    if rand_num<num:
        print(f'The number is smaller than {num},try again')
        num = int(input("Enter your number to guess program number: "))
    elif rand_num>num:
        print(f'The number is bigger than {num},try again')
        num = int(input("Enter your number to guess program number: "))
print("Well done!")


