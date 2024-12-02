from uuid import uuid4, UUID
from currency import Ruble


class Product:
    def __init__(self, name: str, cost: Ruble):
        self._id: UUID = uuid4()
        self._name: str = name
        self._cost: Ruble = cost

    def get_id(self) -> UUID:
        return self._id

    def get_name(self) -> str:
        return self._name

    def set_name(self, name: str):
        self._name: str = name

    def get_cost(self) -> Ruble:
        return self._cost

    def set_cost(self, cost: Ruble):
        self._cost: Ruble = cost

    def __str__(self) -> str:
        return f'{self._name}'
