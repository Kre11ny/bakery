from uuid import UUID
from order.exceptions import NoSuchOrder
from order.order import Order


class OrderStorage:
    def __init__(self):
        self._orders: {UUID: Order} = dict()

    def add_order(self, order: Order):
        self._orders[order.get_id()] = order

    def delete_order(self, order_id: UUID):
        if order_id not in self._orders:
            return

        self._orders.pop(order_id)

    def get_order(self, order_id: UUID) -> Order:
        try:
            return self._orders[order_id]
        except KeyError:
            raise NoSuchOrder

