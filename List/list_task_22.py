import random, sys
file_word = open('C:/Users/Dmoho/Desktop/list_word.txt', 'r+')
str_word = file_word.read()
list_word = str_word.split(',')
rand_word = random.choice(list_word)
print(rand_word)
len_rand_word = int(len(rand_word))
count, bottom_line, str_line, guess = 0, "_", "", bool
for i in range(len_rand_word):
    str_line += bottom_line
    str_line += " "
list_guess_word = str_line.split()
user_letter = str(input(f'Guess the letter {" ".join(list_guess_word)}: '))
if user_letter in rand_word:
    index_user_letter = int(rand_word.find(user_letter))
    guess = True
else:
    guess = False
while True:
    while guess:
        if count > 8:
            sys.exit("Trials are over")
        list_guess_word[index_user_letter] = user_letter
        word_guess_str = (''.join(list_guess_word))
        if rand_word == word_guess_str:
            print("Congratulations!!")
            sys.exit()
        user_letter = str(input(f'Well done, Go one there are {7-count} chances  {word_guess_str}: '))
        if user_letter not in rand_word:
            guess = False
            break
        index_user_letter = int(rand_word.find(user_letter))
        word_guess_str = (''.join(list_guess_word))
        if rand_word == word_guess_str:
            print("Congratulations!!")
            sys.exit()
    while not guess:
        if count > 8:
            sys.exit("Trials are over")
        count += 1
        user_letter = str(input(f'Ouch is painfull!!!Left {7 - count} chances  {" ".join(list_guess_word)}: '))
        if user_letter in rand_word:
            guess = True
            list_guess_word[index_user_letter] = user_letter
            break
        else:
            continue
