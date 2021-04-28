class Animal:
    def __init__(self, name=None, hungry=5.0, energy=5.0):
        self.name = name
        self.hungry_level = hungry
        self.energy_level = energy

    def __str__(self):
        return f'Name - {self.name}\nHungry level - {round(self.hungry_level, 2)}\nEnergy level - {round(self.energy_level, 2)}'

    def eat(self, food_gram = 50):
        for i in range(0, food_gram, 50):
            self.hungry_level -= 1
            if self.hungry_level < 0:
                self.hungry_level = 0
                print(f"{self.name} is full")
                break
            self.energy_level -= 0.5
            if self.energy_level < 0:
                self.energy_level = 0
        return f'energy = {self.energy_level} hungry = {self.hungry_level}'

    def play(self, time_minute = 10):
        for i in range(0, time_minute, 10):
            self.energy_level -= 2.
            if self.energy_level < 0:
                self.energy_level = 0
                self.hungry_level += 2
                if self.hungry_level > 10:
                    self.hungry_level = 10.0
                print(f"Stop play.{self.name} is tired")
                break
            self.hungry_level += 2
            if self.hungry_level > 10:
                self.hungry_level = 10.0
        return f'energy = {self.energy_level} hungry = {self.hungry_level}'

    def rest(self, time_minute = 10):
        for i in range(0, time_minute, 10):
            self.energy_level += 0.5
            if self.energy_level > 10:
                self.energy_level = 10.0
                self.hungry_level += (1 / 3)
                if self.hungry_level > 10:
                    self.hungry_level = 10.0
                print(f'{self.name} finished rest.{self.name} full of energy and want to play with you')
                break
            self.hungry_level += (1/3)
            if self.hungry_level > 10:
                self.hungry_level = 10.0
                print(f'{self.name} is hungry')
                break
        return f'energy = {round(self.energy_level,1)} hungry = {round(self.hungry_level,1)}'
