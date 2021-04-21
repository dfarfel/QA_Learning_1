word=(input("Enter word: "))
index=0
for letter in word:
    index+=1
    for i in range(0,index):
        print(letter,end="")
