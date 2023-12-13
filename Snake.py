import constants as C
from random import choice

class Snake:
    def __init__(self):
        self._direction = choice(list(C.DIRECTIONS.keys()))
        self._length = 1
        self._score = 0

    def eat(self, food: int) -> None:
        self._length += 1
        self._score += food

    def get_state(self) -> dict:
        return {
            "direction": self._direction,
            "length": self._length,
            "score": self._score
        }
    
    def change_direction(self, direction: str) -> None:
        assert direction in C.DIRECTIONS.keys()
        self._direction = direction