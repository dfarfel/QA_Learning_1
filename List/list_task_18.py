user_list=[]
list_letter=[]
count=0
for i in range(5):
    user_str=str(input("Enter your string: "))
    user_list+=user_str.split()
for string in user_list:
    for word in range(1,len(string)+1):
        if word>=4:
            for word in string:
                list_letter.append(word)
            if list_letter[0]==list_letter[-1]:
                count+=1
                list_letter=[]
                break
            else:
                list_letter=[]
print(count)