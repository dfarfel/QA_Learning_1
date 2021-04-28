from unittest import TestCase
from unittest.mock import patch
from Class_object.Class_task_2 import Student


class TestStudent(TestCase):
    @patch("Class_object.Class_task_2.Student.check_pass",return_value=50)
    def test_check_pass(self,mock):
        yosi=Student(50)
        self.assertTrue(yosi.grade==50)

    def test_update_grade(self):
        self.fail()

    def test_print_(self):
        self.fail()
