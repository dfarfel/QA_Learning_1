def palindrom_check(str1):
    str2=str1[::-1]
    if str2==str1:
        str_palindrom=True
    else:
        str_palindrom=False
    return str_palindrom
while True:
    user_str=input("Enter your string and I'll chek is palindrom: ")
    if palindrom_check(user_str):
        print("The string is palindrom!!")
    else:
        print("The string is not palindrom")