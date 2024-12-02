from currency import Ruble
from product import Product
from volume import Milliliter


class Drink(Product):
    def __init__(self, name: str, cost: Ruble, volume: Milliliter):
        super().__init__(name, cost)
        self._volume: Milliliter = volume

    def __str__(self) -> str:
        return f'{self._name} {self._volume}'
