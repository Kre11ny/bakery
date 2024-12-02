from person import Person


class Client(Person):
    def __init__(self, name: str, money: float):
        super().__init__(name)
        self.money: float = money

    def get_money(self) -> float:
        return self.money

    def set_money(self, money: int):
        self.money = money
