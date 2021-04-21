age=int(input("Please enter your age: "))
while 0<=age<=120:
    if 0<=age<=18:
        print("Child")
    elif 19<=age<=60:
        print("adult")
    else:
        print("senior")
    age = int(input("Please enter your age: "))
print("Age is invalid")
