from currency import Ruble
from product import Product


class Backed(Product):
    def __init__(self, name: str, cost: Ruble):
        super().__init__(name, cost)
