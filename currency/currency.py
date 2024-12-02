class Ruble:
    def __init__(self, value: float):
        self.value: float = value

    def __str__(self) -> str:
        return f'{self.value}₽'
