import sys
from Class_object.Class_task_2_3 import Lotto
my_loto=Lotto()
my_loto.show_num()
for i in range(5):
    user_num=int(input("Guess the number: "))
    if 1 > user_num or user_num > 45:
        sys.exit("Invalid number.By")
    if my_loto.check_guess(user_num):
        my_loto.sum_guess_num += 1
print(f'Your winning is - {my_loto.check_win()}')
