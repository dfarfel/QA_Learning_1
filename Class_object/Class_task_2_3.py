import random
class Lotto:
    def __init__(self):
        self.raffle_list=[]
        self.max_jackpot=0
        self.sum_guess_num=0
        self.raffle()
        self.user_input()

    def raffle(self):
        for i in range(6):
            rand_num=random.randint(1,45)
            self.raffle_list.append(rand_num)

    def user_input(self):
        self.max_jackpot=int(input("Enter the winning amount: "))

    def show_num(self):
        for i in self.raffle_list:
            print(i,end=" ")

    def check_guess(self,user_num):
        guess=bool
        if user_num in self.raffle_list:
            guess=True
            return guess
        else:
            guess = False
            return guess

    def check_win(self):
        if self.sum_guess_num <= 1:
            win_amount=0
        elif 2 <= self.sum_guess_num <= 5:
            win_amount=(self.max_jackpot*self.sum_guess_num)/6
        elif self.sum_guess_num == 6:
            win_amount = self.max_jackpot
        return win_amount
