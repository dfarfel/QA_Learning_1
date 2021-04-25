def check_in_range(num,low,high):
    if low<=num<=high:
        print("Your number is in the range")
    else:
        print("There is no number as you choose in this range")
num_1=int(input("Enter number to check: "))
low_1=int(input("Enter low border of the range: "))
high_1=int(input("Enter high border of the range: "))
check_in_range(num_1,low_1,high_1)