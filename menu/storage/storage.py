from backed import Backed
from currency import Ruble
from product import Product
from drink import Drink
from volume import Milliliter


class MenuStorage:
    def __init__(self):
        self._baked_foods: [Backed] = [
            Backed('Круассан', Ruble(50)),
            Backed('Булочка с корицей', Ruble(60)),
            Backed('Торт', Ruble(300)),
            Backed('Пирожное', Ruble(80)),
            Backed('Хлеб', Ruble(40)),
        ]
        self._drinks: [Drink] = [
            Drink('Кофе', Ruble(70), Milliliter(230)),
            Drink('Кофе', Ruble(90), Milliliter(350)),
            Drink('Кофе', Ruble(120), Milliliter(500)),
            Drink('Кофе', Ruble(200), Milliliter(600)),
            Drink('Чай', Ruble(50), Milliliter(230)),
            Drink('Чай', Ruble(70), Milliliter(350)),
            Drink('Чай', Ruble(100), Milliliter(500)),
            Drink('Сок', Ruble(60), Milliliter(200)),
            Drink('Вода', Ruble(30), Milliliter(200)),
        ]

    def get_drinks(self) -> [Drink]:
        return self._drinks

    def get_baked_foods(self) -> [Backed]:
        return self._baked_foods
