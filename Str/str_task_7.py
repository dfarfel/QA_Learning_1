user_sent=str(input("Enter sentence: "))
user_letter=str(input("Enter letter: "))
new_word=''
new_sent=''
list1=user_sent.split()
for word in list1:
    for letter in word:
        if user_letter==letter:
            new_word+=letter.capitalize()
        else:
            new_word+=letter
    new_sent+=f'{new_word} '
    new_word=''
print(new_sent)