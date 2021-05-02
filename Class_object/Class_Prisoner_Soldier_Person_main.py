from Class_object import Class_Person,Class_Prisoner,Class_Soldier
user_num = int(input("Enter the number of man: "))
list_1=[]
for i in range(user_num):
    user_choice=int(input("Who we should to in?: Citizen - 1. Soldier - 2. Prisoner - 3: "))
    if user_choice == 1:
        pers_1=Class_Person.Person(int(input("Enter id: ")),input("Enter name: "),int(input("Enter age: ")))
        list_1.append(pers_1)
    elif user_choice == 2:
        sold_1 = Class_Soldier.Soldier(int(input("Enter id: ")),input("Enter name: "),int(input("Enter age: ")),input("Enter rank: "),input("Enter unit: "))
        list_1.append(sold_1)

    elif user_choice == 3:
        pris_1=Class_Prisoner.Prisoner(int(input("Enter id: ")),input("Enter name: "),int(input("Enter age: ")),input("Enter name of prison: "),input("Enter the crime: "),int(input("How many month in prison?:")))
        list_1.append(pris_1)

print(list_1)