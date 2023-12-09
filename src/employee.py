"""
xdcfgvhbjnkml
"""

from src.services import CURRENCIES, Salary
from datetime import datetime


class Date:
    '''
    дескриптор
    '''

    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self._name]

    def __set__(self, instance, value):
        instance.__dict__[self._name] = datetime.strptime(value, '%Y:%m:%d')


class Employee:

    birth_date = Date()
    start_date = Date()

    def __init__(self, name, surname, age, birth_date, start_date, salary: Salary | None = None):

        self.name = name
        self.surname = surname
        self._age = age
        self.__salary = salary
        self.birth_date = birth_date
        self.start_date = start_date

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name.upper()

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def print_initials(self):
        print(f'name: {self.name}, surname: {self.surname}, Age: {self.age}')

    @staticmethod
# декоратор, чтобы не было ошибки...метод статический тк нет селф в арг методв
    def say_hello():
        print('hi')

    def set_salary(self, amount, currency):
        self.__salary = Salary(amount=amount, currency=currency)

    def get_salary(self, currency=CURRENCIES.RUBLE):
        if self.__salary and currency == self.__salary.currency:
            return self.__salary.amount
        return self._count_salary(currency)

    def _count_salary(self, currency):
        match (currency, self.__salary.currency):
            case (CURRENCIES.RUBLE, CURRENCIES.DOLLAR): return self.__salary.amount * 88
            case (CURRENCIES.DOLLAR, CURRENCIES.RUBLE): return self.__salary.amount / 88
            case _: raise AttributeError
        #raise error for final impossible case


class Programmer(Employee):
    pass


class Manager(Employee):
    pass


class CEOManager(Manager):
    pass


class HRManager(Manager):
    pass


class FrontendEngineer(Programmer):
    pass


class BackendEngineer(Programmer):
    pass


class QAEngineer(Programmer):
    pass


def print_employee_type(empl_obj):
    print(f'Does current employee belong to Employee type? {isinstance(empl_obj, Employee)}')
    print(f'Employee {empl_obj.name} is of {type(empl_obj)} type')
    print(f"Employee's salary is {empl_obj.count_salary()}")
