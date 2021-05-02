from Class_object.Class_Person import Person
class Soldier(Person):
    def __init__(self, id, name=None, age=None, rank=None,unit=None):
        Person.__init__(self,id, name, age)
        self.rank = rank
        self.unit = unit
    def __repr__(self):
        return Person.__repr__(self) + f'.Rank - {self.rank}. Unit - {self.unit}'


