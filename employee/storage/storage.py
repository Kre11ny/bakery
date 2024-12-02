from currency import Ruble
from employee import Employee, Cashier, Baker, Manager


class EmployeeStorage:
    def __init__(self):
        self._employees = [
            Cashier('Alice', Ruble(100000)),
            Baker('Bob', Ruble(100000)),
            Manager('Charlie', Ruble(150000)),
        ]

    def get_employees(self) -> [Employee]:
        return self._employees

    def get_cahier(self) -> Cashier:
        for emp in self._employees:
            if isinstance(emp, Cashier):
                return emp

    def get_baker(self) -> Baker:
        for emp in self._employees:
            if isinstance(emp, Baker):
                return emp

    def get_manager(self) -> Manager:
        for emp in self._employees:
            if isinstance(emp, Manager):
                return emp
