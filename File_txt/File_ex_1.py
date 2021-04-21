open_file=open('C:/Users/dmoho/Desktop/data.txt','a+')
for i in range (5):
    open_file.write("my first txt file\n")
print(open_file.read())
open_file.close()
print(open_file.closed)