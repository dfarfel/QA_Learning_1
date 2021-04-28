class Animal:
    def __init__(self, name=None, hungry=5.0, energy=5.0):
        self.name = name
        self.hungry_level = hungry
        self.energy_level = energy

    def __str__(self):
        return (f'Name - {self.name}\nHungry level - {self.hungry_level}\nEnergy level - {self.energy_level}')

    def eat(self,food_grm = 50):
        for i in range(0, food_grm, 50):
            self.hungry_level -= 1
            if self.hungry_level < 0:
                self.hungry_level = 0
                print(f"{self.name} is full")
                break
            self.energy_level -= 0.5
            if self.energy_level < 0:
                self.energy_level = 0

    def play(self, time_minute = 1):
        for i in range(0, time_minute):
            self.energy_level -= 0.2
            if self.energy_level < 0:
                self.energy_level = 0
                print(f"Stop play.{self.name} is tired")
                break
            self.hungry_level += 0.2
            if self.hungry_level > 10:
                self.hungry_level = 10

    def rest(self, time_minute = 3):
        for i in range(0,time_minute, 3):
            self.energy_level += 0.15
            if self.energy_level > 10:
                self.energy_level = 10
                print(f'{self.name} finished rest.{self.name} full of energy and want to play with you')
                break
            self.hungry_level += 0.1
            if self.hungry_level > 10:
                self.hungry_level = 10
                print(f'{self.name} is hungry')
                break

