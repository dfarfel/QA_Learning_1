import random
ran_num=random.randrange(1000,9999)
user_num=int(input("Guess the number: "))
while user_num!=ran_num:
    user_num = int(input("Guess the number: "))

