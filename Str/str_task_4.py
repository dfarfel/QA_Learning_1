word1=str(input("Enter a first word: "))
word2=str(input("Enter a second word: "))
count=0
for letter in word1:
    if word2.count(letter)>0:
        count+=1
print(f'There is {count} same letters in your words')
