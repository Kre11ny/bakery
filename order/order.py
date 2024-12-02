from __future__ import annotations
from uuid import UUID, uuid4
from backed import Backed
from currency import Ruble
from drink import Drink
from order.exceptions import NoSuchOrderPosition
from order.oreder_entity import OrderEntity


class Order:
    def __init__(self):
        self._id: UUID = uuid4()
        self._positions: {UUID: OrderEntity} = dict()

    def get_id(self) -> UUID:
        return self._id

    def add_position(self, product_id: UUID, name: str, cost: Ruble, count: int):
        if product_id not in self._positions:
            self._positions[product_id] = OrderEntity(name, cost, count)
            return

        self._positions[product_id].add_count(count)

    def remove_position(self, product_id: UUID, count: int):
        if product_id not in self._positions:
            raise NoSuchOrderPosition

        self._positions.pop(product_id)

    def det_drinks(self) -> [Drink]:
        drinks: [Drink] = []
        for item in self._positions:
            if isinstance(item, Drink):
                drinks.append(item)

        return drinks

    def det_backed(self) -> [Backed]:
        backed: [Backed] = []
        for item in self._positions:
            if isinstance(item, Backed):
                backed.append(item)

        return backed

    def total_cost(self) -> float:
        total_cost = 0
        for v in self._positions.values():
            total_cost += v.cost()

        return total_cost

    def __str__(self) -> str:
        res = ''
        for v in self._positions.values():
            res += v.get_name()
            res += '\n'

        res += f'Общая стоимость: {self.total_cost()}'

        return res
