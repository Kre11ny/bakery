from person import Person


class Client(Person):
    def __init__(self, name: str, money: int):
        super().__init__(name)
        self.money: int = money

    def get_money(self) -> int:
        return self.money

    def set_money(self, money: int):
        self.money = money
