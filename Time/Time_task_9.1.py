import datetime,time
name=input("Enter your name: ")
birthday=int(input("Enter your age: "))
now=datetime.datetime.now()
years=now.strftime("%Y")
birth_year=int(years)-birthday
birth_year_100=birth_year+100
print(f'Dear {name}, in {birth_year_100} you will be 100 years old')

