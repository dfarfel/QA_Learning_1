def while_true():
    if user_letter in rand_word:
        index_user_letter = int(rand_word.find(user_letter))
        guess = True
    while guess:
        if count > 8:
            sys.exit("Trials are over")
        list_guess_word.insert(index_user_letter, user_letter)
        user_letter = str(input(f'Well done, Go one there are {7 - count} chances  {" ".join(list_guess_word)}: '))
        if user_letter not in rand_word:
            guess = False
        word_guess_str = (''.join(list_guess_word))
        if rand_word == word_guess_str:
            print("Congratulations!!")
            sys.exit()