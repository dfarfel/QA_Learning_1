#Index of bigest number in input
index=0
num_1=0
for i in range(1,8):
    num=int(input("enter number: "))
    index+=1
    if num_1<num:
        num_1=num
        big_index=index
print(big_index)

