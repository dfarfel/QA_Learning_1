from Class_object.Class_task_2_2 import Bus
user_num_seats=int(input("Enter the number of seats: "))
bus_1=Bus()
bus_1.conctructor(user_num_seats)
user_choise=int(input("What should we do? 1 - put passenger on the bus. 2 - drop passenger off the bus. 3 - bus information 0 - End of program: "))
while user_choise != 0:
    if user_choise == 1:
        bus_1.getOn_2(str(input("Enter the name of a passenger: ")))
        user_choise=int(input("What should we do? 1 - put passenger on the bus. 2 - drop passenger off the bus. 3 - bus information 0 - End of program: "))

    elif user_choise == 2:
        bus_1.getOf(str(input("Enter the name of a passenger: ")))
        user_choise = int(input("What should we do? 1 - put passenger on the bus. 2 - drop passenger off the bus. 3 - bus information 0 - End of program: "))
    elif user_choise == 3:
        print(bus_1)
        user_choise = int(input(
            "What should we do? 1 - put passenger on the bus. 2 - drop passenger off the bus. 3 - bus information 0 - End of program: "))