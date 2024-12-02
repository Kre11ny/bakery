class Ruble:
    def __init__(self, value: float):
        self._value: float = value

    def __str__(self) -> str:
        return f'{self._value}₽'

    @property
    def value(self) -> float:
        return self._value