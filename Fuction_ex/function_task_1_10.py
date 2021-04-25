def pass_grade(grade):
    passg=bool
    if 70<=grade<=100:
        passg=True
    else:
        passg=False
    return passg



for i in range(5):
    user_grade=int(input("Enter your grade: "))
    if pass_grade(user_grade):
        print("Passed")
    else:
        print("Failed")