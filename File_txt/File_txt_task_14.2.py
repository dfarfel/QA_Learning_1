with open('C:/Users/dmoho/Desktop/.story.txt','r+') as file:
    count_line=0
    count_word_all=0
    count_word=0
    count_letter=0
    for line in file:
        if line[0]!="T":
            count_line+=1
        words=line.split()
        for word in words:
            count_word_all+=1
            if word=="the" or word=="The":
                count_word+=1
            for letter in word:
                if letter=="a":
                    count_letter+=1
print(f'Quantity of lines without letter "T" in the biginning is {count_line}\nQuantity of words "the" or "The" in the text is {count_word}\nQuantity of words in the text is {count_word_all}')