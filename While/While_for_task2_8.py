s=[]
prime_number=0
for i in range(5):
    num=int(input("Enter your number: "))
    if num==2 or num==3 or num==5 or num==7 :
        prime_number=num
        s.append(prime_number)
    elif num<2:
        continue
    elif num%2==0 or num%3==0 or num%5==0 or num%7==0 or num%9==0:
        continue
    else:
        prime_number=num
        s.append(prime_number)
print(min(s))