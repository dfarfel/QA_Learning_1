import random
name=str(input("Enter your name: "))
password=''
for i in range(6):
    random_letter=random.choice(name)
    password+=random_letter
print(password)

