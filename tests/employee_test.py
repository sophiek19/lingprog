import unittest
from src.employee import Employee

class EmployeeBaseTest(unittest.TestCase):

    def test_create_employee_ideal(self):
        instance = Employee('max', 'long', 25, birth_date='2003:06:07', start_date='2022:01:10')
        self.assertEqual(instance.name, 'MAX')
        self.assertEqual(instance.age, 25)
