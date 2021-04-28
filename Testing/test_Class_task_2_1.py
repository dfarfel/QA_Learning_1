from unittest import TestCase
from Class_object.Class_task_2_1 import Animal


class TestAnimal(TestCase):
    def setUp(self):
        self.Emi=Animal("Emi")
        self.Senya=Animal("Senya")
    def test_eat(self):
        self.assertEqual(self.Emi.eat(100),"energy = 4.0 hungry = 3.0")
        self.assertEqual(self.Senya.eat(500),"energy = 2.5 hungry = 0")

    def test_play(self):
        self.assertEqual(self.Emi.play(20),"energy = 1.0 hungry = 9.0")
        self.assertEqual(self.Senya.play(30),"energy = 0 hungry = 10.0")

    def test_rest(self):
        self.assertEqual(self.Emi.rest(30),"energy = 6.5 hungry = 6.0")
        self.assertEqual(self.Senya.rest(120),"energy = 10.0 hungry = 8.7")
