from currency import Ruble
from employee import Employee, Cashier, Baker, Manager
from product import Product
from drink import Drink
from volume import Milliliter


class Storage:
    def __init__(self):
        self._baked_foods: [Product] = [
            Product('Круассан', Ruble(50)),
            Product('Булочка с корицей', Ruble(60)),
            Product('Торт', Ruble(300)),
            Product('Пирожное', Ruble(80)),
            Product('Хлеб', Ruble(40)),
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
        self._employees = [
            Cashier('Alice', Ruble(100000)),
            Baker('Bob', Ruble(100000)),
            Manager('Charlie', Ruble(150000)),
        ]

    def get_drinks(self) -> [Drink]:
        return self._drinks

    def get_baked_foods(self) -> [Product]:
        return self._baked_foods

    def get_employees(self) -> [Employee]:
        return self._employees

    def get_cahier(self) -> Cashier:
        for emp in self._employees:
            if isinstance(emp, Cashier):
                return emp

    def get_baker(self) -> Baker:
        for emp in self._employees:
            if isinstance(emp, Baker):
                return emp

    def get_manager(self) -> Manager:
        for emp in self._employees:
            if isinstance(emp, Manager):
                return emp
