sum=0
for i in range(1,5):
    num = int(input("Pleasse enter the number: "))
    if num>10:
        right_num=num%10
    else:
        right_num=0
    sum+=right_num
print (sum)