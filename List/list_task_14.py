num=int(input("Enter number: "))
list1=[]
for i in range(1,num+1):
    if num%i==0 or num%i==num:
        list1.append(i)
print(list1)