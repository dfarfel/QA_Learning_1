def convert():
    age=int(input("Please enter your age: "))
    if 0<=age<=18:
        print("Child")
    else:
        if 19<=age<=60:
            print("Adult")
        else:
            if 61<=age<=120:
                print("senior")
            else:
                print("ERROR!")
convert()
while True:
    end_prog=input('One more? [1/0]: ')
    if end_prog == "1":
        convert()
    else:
        break