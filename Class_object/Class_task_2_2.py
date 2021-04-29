import sys
class Bus:
    def __init__(self):
        self.seats=0
        self.dict_seats={}
        self.num_passenger = 0

    def conctructor(self,seats):
        self.seats=seats
        for i in range(1,self.seats+1):
            self.dict_seats.update({i:"Free"})
        return self.dict_seats

    def getOn(self, passenger_name=None):
        self.num_passenger += 1
        if self.num_passenger > self.seats:
            sys.exit(f'Sorry dear {passenger_name}. There is no free seat on the bus')
        free_list = list(self.dict_seats.values())
        free_num_seat = int(free_list.index("Free"))+1
        self.dict_seats.update({free_num_seat : passenger_name})



    def getOf(self,passenger_name=None):
        self.num_passenger -= 1
        close_list = list(self.dict_seats.values())
        if passenger_name in close_list:
            close_num_seat = int(close_list.index(passenger_name) + 1)
            self.dict_seats.update({close_num_seat: "Free"})
        else:
            print(f'Passenger {passenger_name} is not on the bus')
    def __str__(self):
        return f'Number of seats on the bus - {self.seats}\nNumber of passenger - {self.num_passenger}'\
               f'\nFree seats - {self.seats-self.num_passenger}'\
               f'\nOther details - {self.dict_seats}'

