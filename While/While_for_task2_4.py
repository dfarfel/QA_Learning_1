# Output left digit don't matter how many digits
while True:
    num=input("Enter number: ")
    sum_digit=0
    for digit in num:
        sum_digit+=1
    left_digit=int(num)//10**(int(sum_digit)-1)
    print(left_digit)