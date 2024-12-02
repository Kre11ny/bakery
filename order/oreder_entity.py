from currency import Ruble


class OrderEntity:
    def __init__(self, name: str, cost: Ruble, count: int):
        self._name: str = name
        self._cost: Ruble = cost
        self._count: int = count

    def products_count(self) -> int:
        return self._count

    def cost(self) -> float:
        return self._count * self._cost.value

    def get_name(self) -> str:
        return self._name

    def add_count(self, count: int):
        self._count += count
