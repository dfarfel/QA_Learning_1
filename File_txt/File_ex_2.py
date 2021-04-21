t=["pizda ","tobi ","a ","ne ","meni "]
with open('C:/Users/dmoho/Desktop/data.txt','w+') as file:
    file.writelines(t)
with open('C:/Users/dmoho/Desktop/data.txt','w') as file_1:
    # for i in range(5):
    #     file_1.write(f"{r_data}\n")
          #file_1.writelines(t)
    #print(file_1.tell())
    file_1.seek(0)
    file_1.seek(0,2)
    file_1.writelines(t)

