list1=[num for i in range(5)]
for i in range(5):
    num=int(input("Enter number: "))
    list1.append(num)
print(f'Smaller number is {min(list1)}\nLargest number is {max(list1)}\nAvarage is {sum(list1)/len(list1)}')