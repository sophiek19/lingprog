"""
Startup for employee base
"""

from src.employee import (Employee, Programmer, Manager, HRManager, CEOManager, QAEngineer, FrontendEngineer,
                          BackendEngineer, print_employee_type)
from src.services import Salary,CURRENCIES

if __name__ == '__main__':

    employee_1 = Programmer('MAX', 'FirstSurname', 25, birth_date='2003:06:07', start_date='2022:01:10')
    # employee_1_1 = FrontendEngineer('FirstName', 'FirstSurname', 28)
    # employee_1_2 = BackendEngineer('FirstName', 'FirstSurname', 29)
    # employee_1_3 = QAEngineer('FirstName', 'FirstSurname', 28)
    #
    # employee_2 = Manager('SecondName', 'SecondSurname', 65)
    # employee_2_1 = CEOManager('SecondName', 'SecondSurname', 65)
    # employee_2_2 = HRManager('SecondName', 'SecondSurname', 65)
    #
    # employees = [employee_1, employee_1_1, employee_1_2, employee_1_3, employee_2, employee_2_1, employee_2_2]
    #
    # for employee in employees:
    #     print_employee_type(employee)
    #
    # salary_obj = Salary(amount=10000, currency=CURRENCIES.RUBLE)
    print(employee_1.birth_date)