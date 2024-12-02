from currency import Ruble
from employee import Employee


class Baker(Employee):
    def __init__(self, name: str, salary: Ruble):
        super().__init__(name, salary)
        self._position: str = 'Baker'

    def set_position(self, position: str):
        self._position: str = position

    def get_position(self) -> str:
        return self._position

    def __str__(self):
        return f'{self.get_position()}: {self.get_name()}'
