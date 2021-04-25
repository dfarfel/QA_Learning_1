def check_age(age):
    age_group=""
    if 0<=age<=18:
        age_group="Child"
    elif 19<=age<=60:
        age_group="Adult"
    elif 61<=age<=120:
        age_group="Senior"
    else:
        age_group="ERROR!"
    return age_group

for i in range(5):
    user_age=int(input("Enter your age: "))
    print(check_age(user_age))