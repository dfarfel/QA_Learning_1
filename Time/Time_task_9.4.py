import datetime
while True:
    num=input("Enter your number: ")
    if 1<=int(num)<=7:
        first=datetime.date(2021,4,10)
        day=first+datetime.timedelta(days=int(num))
        week=day.strftime('%A')
        print(week)
    else:
        print("You can use only 1 between 7 ")

