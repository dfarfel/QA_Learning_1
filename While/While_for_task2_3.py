num=int(input("Enter your number: "))
num_1=num
while num>0:
    if num_1>num:
        num_1=num
    num = int(input("Enter your number: "))
print(num_1)
