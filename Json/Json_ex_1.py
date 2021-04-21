import json
name_1=input("Enter name 1: ")
height_1=input("Enter hieght 1: ")
name_2=input("Enter name 2: ")
height_2=input("Enter hieght 2: ")
name_3=input("Enter name 3: ")
height_3=input("Enter hieght 3: ")
if height_1.isnumeric() and height_2.isnumeric() and height_3.isnumeric():
    json_data={name_1:height_1,name_2:height_2,name_3:height_3}
    with open("json_file.json",'w+') as jfile:
        json.dump(json_data,jfile)
        jfile.close()
    with open("json_file.json","r+") as jfile_r:
        jobject=json.load(jfile_r)
        print(jobject)
        a=jobject[name_1]
        b=jobject[name_2]
        c=jobject[name_3]
        print(b)
else:
    print("Height must be number!")


