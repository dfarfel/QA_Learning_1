def convert():
    num=input("Please enter number of computers: ")
    while num.isnumeric():
        print(int(num)*2)
        num = input("Please enter number of computers: ")
    while not num.isnumeric():
        print("Invalid!")
        num = input("Please enter number of computers: ")
        convert()
convert()
