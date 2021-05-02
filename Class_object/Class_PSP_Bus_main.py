from Class_object.Class_task_2_2_improved import Bus_person
from Class_object.Class_Person import Person
from Class_object.Class_Soldier import Soldier
from Class_object.Class_Prisoner import Prisoner

user_num_seats = int(input("Enter the number of seats: "))
bus_1 = Bus_person()
bus_1.constructor(user_num_seats)
user_choice_1 = int(
    input("What should we do? 1 - put passenger on the bus. 2 - drop passenger off the bus. 0 - Ebd program: "))
while user_choice_1 != 0:

    if user_choice_1 == 1:
        user_choice_1_1 = input("Who gonna get on? c - Citizen. s - Soldier. p - Prisoner: ")
        user_id_on = int(input("Enter the id: "))
        user_name = input("Enter the name: ")
        user_age = int(input("Enter the age: "))
        if user_choice_1_1 == "c":
            per_1 = Person(user_id_on, user_name, user_age)
            bus_1.getOn(per_1)

        elif user_choice_1_1 == "s":
            user_rank = input("Enter the rank: ")
            user_unit = input("Enter the unit: ")
            sol_1 = Soldier(user_id_on, user_name, user_age, user_rank, user_unit)
            bus_1.getOn(sol_1)

        elif user_choice_1_1 == "p":
            user_prison_name = input("Enter a name of the prison: ")
            user_crime = input("Enter the crime: ")
            user_time = int(input("How many month in prison?: "))
            pris_1 = Prisoner(user_id_on, user_name, user_age, user_prison_name, user_crime, user_time)
            bus_1.getOn(pris_1)
    elif user_choice_1 == 2:
        user_id_off = int(input("Enter the id: "))
        man_1 = Person(user_id_off)
        bus_1.getOf(man_1)

    else:
        user_choice_1 = int(input(
            "Invalid Enter!\nWhat should we do? 1 - put passenger on the bus. 2 - drop passenger off the bus. 0 - Ebd program: "))

    print(bus_1)

    user_choice_1 = int(
        input("What should we do? 1 - put passenger on the bus. 2 - drop passenger off the bus. 0 - End program: "))
