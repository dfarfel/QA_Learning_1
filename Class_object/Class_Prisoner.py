from Class_object.Class_Person import Person
class Prisoner(Person):
    def __init__(self, id, name= None, age=None, prison_name=None, crime=None, month_in_prison=None):
        Person.__init__(self,id, name, age)
        self.prison_name = prison_name
        self.crime = crime
        self.month_in_prison = month_in_prison

    def __repr__(self):
       return Person.__repr__(self)+ f' Name of the prison - {self.prison_name}' \
               f' Done crime - {self.crime}. Month in prison - {self.month_in_prison}'