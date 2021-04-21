num1=input(("enter number of computers: "))
if num1.isnumeric():
    num1=int(num1)
else:
    import sys
    sys.exit("Enter is invalid")
if num1=='':
    num1=15
print(num1*2)



