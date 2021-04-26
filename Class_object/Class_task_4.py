class Circle:
    def __init__(self):
        self.radius = 0
        self.pi = 3.14
    def area(self):
        A = self.pi * (self.radius ** 2)
        return A
    def circumference(self):
        C = 2 * self.pi * self.radius
        return C