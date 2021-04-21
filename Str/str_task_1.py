word=str(input("Enter your word: "))
str2=''
for letter in word:
    if letter=="a" or letter=='A':
        continue
    else:
        str2+=letter
print(str2)