my_dict={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
user_key=input("Enter your key for dictionary: ")
keys=list(my_dict.keys())
if keys.count(user_key)>0:
    print("There is your key in the dictionary")
else:
    print("There is NOT your key in the dictionary")

