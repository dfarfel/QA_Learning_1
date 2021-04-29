
class Bus_person:
    def __init__(self):
        self.num_seats=0
        self.seats=[]
        self.num_passenger = 0

    def conctructor(self,seats):
        self.num_seats=seats
        for i in range(self.num_seats):
            self.seats.append("Free")
        return self.seats

    def getOn(self, person):
        if self.num_passenger <= len(self.seats):
            seat_index=self.seats.index("Free")
            self.seats[seat_index] = person
            self.num_passenger += 1
        else:
            print("There is no place in the bus")

    def getOf(self,person):
        if person in self.seats:
            index_person=self.seats.index(person)
            self.seats[index_person]="Free"
            self.num_passenger -= 1
        else:
            print(f"There are no passenger {person.name}")
        return self.seats
    def __str__(self):
        return f'Number of seats on the bus - {self.num_seats}\nNumber of passenger - {self.num_passenger}'\
               f'\nFree seats - {self.num_seats-self.num_passenger}'\
               f'\nOther details - {self.seats}'

