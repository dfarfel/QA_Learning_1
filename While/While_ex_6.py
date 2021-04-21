while True:
    dd=int(input("Please enter the day: "))
    while 1>dd or 31<dd:
        print("The day is invalid")
        dd = int(input("Please enter the day: "))
    if dd<10:
        dd='0'+str(dd)
    mm=int(input("Please enter the month: "))
    while 1>mm or 12<mm:
        print("The month is invalid")
        mm = int(input("Please enter the month: "))
    if mm<10:
        mm='0'+str(mm)
    yy=int(input("Please enter the year: "))
    while yy<1950 or yy>2025:
        print("The year is invalid")
        yy = int(input("Please enter the year: "))
    yy=yy%100
    if yy<10:
        yy='0'+str(yy)
    print(f'{dd}/{mm}/{yy}')





