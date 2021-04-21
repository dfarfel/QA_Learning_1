import datetime, time
t=datetime.datetime.now()#return current time
t_birthday=datetime.datetime(2021,6,28,0,0,1)#Return time that you set
datetime.timedelta(days=10,hours=10)#Enable finction of math acts on date only for day/hour/second/milisecond/micro
b=datetime.date(1999,6,28)
fif=datetime.time(2,3,5)
now=t.strftime('%Y/%m/%d %H:%M:%S  %A')#return day/year/month/sexond from list of time
print(now)
print(f'{t}\n{t_birthday}')

