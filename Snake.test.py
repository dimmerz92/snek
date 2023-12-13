import constants as C
from Snake import Snake

def init_snake(snake: Snake):
    assert snake._direction in C.DIRECTIONS.keys(), "direction is not valid"
    assert snake._length == 1, "incorrect starting length"
    assert snake._score == 0, "incorrect starting score"

def eat_food(snake: Snake):
    snake.eat(10)
    assert snake._length == 2, "incorrect length after eating"
    assert snake._score == 10, "incorrect score after eating"

def check_state(snake: Snake):
    state = snake.get_state()
    assert state["length"] == 2, "incorrect length in state"
    assert state["score"] == 10, "incorrect score in state"
    assert state["direction"] in C.DIRECTIONS.keys(), "incorrect direction in state"

if __name__ == "__main__":
    snake = Snake()
    init_snake(snake)
    eat_food(snake)
    check_state(snake)