#build series of Fibonachi with quantity of numbers which user set
fib_1=0 #first variable (First at series)
fib_2=1#second variable (second ar series)
fib_3=0 #third variable( Sum of first and second variable therefore third at least)
string_fib="0 " #
num=int(input("Enter quantity of numbers in series of Fabinachi: "))
for i in range(1,num):
    fib_3=fib_1+fib_2
    string_fib=string_fib+str(fib_3)+" "
    fib_2 = fib_1
    fib_1=fib_3
print(string_fib)







