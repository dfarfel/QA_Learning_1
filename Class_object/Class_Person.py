class Person:
    def __init__(self,id,name=None,age=None):
        self.id = id
        self.name = name
        self.age = age
    def __repr__(self):
        return f'Id - {self.id}. Name - {self.name}. Age - {self.age}'

    def __eq__(self, other):
        if other == "Free":
            return False
        if int(self.id) == int(other.id):
            return True
        else:
            return False