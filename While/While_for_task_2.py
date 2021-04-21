password=input("Please enter your password: ")
password_ver=input("Please enter your password secondly: ")
while password_ver!=password:
    for i in range(1,5):
        password_ver = input("Verification password is not the same.Please enter your password secondly: ")
    import sys
    sys.exit("Too many trials")
print("Password changed successfully ")
