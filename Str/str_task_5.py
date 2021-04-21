sent=str(input("Enter your sentence: "))
word=str(input("Enter your word: "))
list1=[]
if word in sent:
    index = sent.index(word[0],sent.index(word))
    for i in range(len(word)):
        list1.append(index+i)
    print(list1)
else:
    print("There is no such word in your sentence ")



