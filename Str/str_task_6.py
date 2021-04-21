sent=str(input("Enter your sentence: "))
Str=''
list1=[]
list1=sent.split()
for word in list1:
    Word=word.capitalize()
    Str+=f'{Word} '
print(Str)