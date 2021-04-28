class Person:
    def __init__(self):
        self.name = None
        self.age = 0
        self.child_num = 0
    def print_(self):
        print(f"Name of the person - {self.name}\nAge of the person - {self.age}\nNumber of child - {self.child_num}")

    def has_children(self):
        if self.child_num > 0:
            has = True
        else:
            has = False
        return has
    def age_group(self):
        if 0 <= self.age <= 18:
            group = "child"
        elif 19 <= self.age <= 60:
            group = "Adult"
        elif 61 <= self.age <=120:
            group = "Senior"
        else:
            group = None
        return group