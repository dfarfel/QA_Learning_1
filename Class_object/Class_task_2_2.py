class Bus:
    def __init__(self):
        self.seats=0
        self.dict_seats={}
        self.num_passenger=0

    def conctructor(self):
        user_seat = int(input("Enter the number of seats: "))
        self.seats=user_seat
        for i in range(1,self.seats+1):
            self.dict_seats.update({i:"Free"})
        return self.dict_seats

    def getOn(self,passenger_name=None):
        free_list = list(self.dict_seats.values())
        free_num_seat = int(free_list.index("Free"))+1
        self.dict_seats.update({free_num_seat : passenger_name})
        if free_num_seat> self.seats:
            print(f'Sorry dear {passenger_name}. There is no free seat on the bus')

    def getOf(self,passenger_name=None):
        close_list = list(self.dict_seats.values())
        if not passenger_name in close_list:
            print(f'Passenger {passenger_name} is not on the bus')

        close_num_seat = int(close_list.index({passenger_name})+1)
        self.dict_seats.update({close_num_seat : "Free"})

    def __str__(self):
        return f'Number of seats on the bus - {self.seats}\nNumber of passenger - {self.num_passenger}' \
               f'\nOther details - {self.dict_seats}'

