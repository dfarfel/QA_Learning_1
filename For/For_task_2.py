sum=0
avarage=0
count=0
for i in range(1,7):
    num = int(input("Please enter number: "))
    if num%2==0:
        count+=1
        sum+=num
        avarage=sum/count
print("Sum = "+str(sum)+'\n'"Avarage = "+str(avarage))