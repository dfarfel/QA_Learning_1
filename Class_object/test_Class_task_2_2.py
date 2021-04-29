from unittest import TestCase
from Class_object.Class_task_2_2 import Bus


class TestBus(TestCase):
    def setUp(self):
        self.bus_1=Bus(4)
        self.bus_2=Bus(1)
    def test_conctructor(self):
        self.assertEqual(self.bus_1.conctructor(),{1:"Free",2:"Free",3:"Free",4:"Free"})
        self.assertNotEqual(self.bus_2.conctructor(),{0:"Free","Free":1,1:"free"})


    def test_get_on(self):
        self.assertEqual(self.bus_1.getOn("Dima"),{1:"Dima",2:"Free",3:"Free",4:"Free"})

        #self.assertFalse(self.bus_1.getOn(a))

    def test_get_of(self):
        self.fail()
