from random import randint
a = 0
b = 100
random_num = randint(a, b)
print(random_num)
question = str(input("Smaller or bigger?: "))
while question != "=":
    while question == "<":
        b = random_num-1
        random_num = randint(a, b)
        print(random_num)
        question = str(input("Smaller or bigger?: "))
    while question == ">":
        a = random_num+1
        random_num = randint(a, b)
        print(random_num)
        question = str(input("Smaller or bigger?: "))
print("I did it!")
