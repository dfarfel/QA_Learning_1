from Class_object.Class_task_2_2_improved import Bus_person
from Class_Person import Person
user_num_seats=int(input("Enter the number of seats: "))
bus_1=Bus_person()
bus_1.constructor(user_num_seats)
user_choise=int(input("What should we do? 1 - put passenger on the bus. 2 - drop passenger off the bus. 3 - bus information 0 - End of program: "))
while user_choise != 0:
    if user_choise == 1:
        person=Person(int(input("Enter id: ")),input("Enter name: "),int(input("Enter age: ")))
        bus_1.getOn(person)

    elif user_choise == 2:
        person = Person(int(input("Enter id: ")))
        bus_1.getOf(person)

    elif user_choise == 3:
        print(bus_1)

    user_choise = int(input("What should we do? 1 - put passenger on the bus. 2 - drop passenger off the bus. 3 - bus information 0 - End of program: "))