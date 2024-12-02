class Milliliter:
    def __init__(self, volume: int):
        self._volume: int = volume

    def get_volume(self) -> int:
        return self._volume

    def __str__(self) -> str:
        return f'{self._volume}ml'
