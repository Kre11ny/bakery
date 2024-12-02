class NoSuchOrder(Exception):
    def __init__(self, room: int):
        super().__init__('Такого заказа не существует')


class NoSuchOrderPosition(Exception):
    def __init__(self, room: int):
        super().__init__('Такой позиции в заказе не существует')
