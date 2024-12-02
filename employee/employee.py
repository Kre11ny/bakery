from uuid import uuid4, UUID
from currency import Ruble
from person import Person


class Employee(Person):
    def __init__(self, name: str, salary: Ruble):
        super().__init__(name)
        self._id: UUID = uuid4()
        self._salary: Ruble = salary

    def get_id(self) -> UUID:
        return self._id

    def set_salary(self, salary: Ruble):
        self._salary: Ruble = salary

    def get_salary(self) -> Ruble:
        return self._salary

    def __str__(self):
        return f"Employee Name: {self.get_name()}"

