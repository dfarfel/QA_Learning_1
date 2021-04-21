str1=str(input("Enter string: "))
str2=""
str2+=str1[0]
str2+=str1[-1]
for i in range(1,len(str1)+1):
    print(str2)