day=int(input("Please enter your day of birth: "))
month=int(input("Please enter your month of birth: "))
year=int(input("Please enter your year of birth: "))
if 1<=day<=31 and 1<=month<=12 and year==2000:
    print(f'{day}/{month}/{"00"}')
else:
    if 1<=day<=31 and 1<=month<=12 and (1950<=year<=1999 or 2001<=year<=2020):
            print(f'{day}/{month}/{year%100}')
    else:
            print ("Error")

