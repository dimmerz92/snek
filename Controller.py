import sys
import constants as C
from Display import Display
from Gameboard import Gameboard
from Snake import Snake

class Controller:
    def __init__(self, size: int = 20):
        self._gameboard = Gameboard(size)
        self._snake = Snake()
        self._display = Display(size)
    
    def start_game(self):
        running = True
        game_over = False
        while running:
            key = self._display.get_key_events()
            if key == "QUIT":
                sys.exit()
            elif key in C.DIRECTIONS.keys():
                self._snake.change_direction(key)
            
            if not game_over:
                snake_state = self._snake.get_state()
                slither = self._gameboard.move_snake(snake_state["direction"])
                if slither == C.QUIT:
                    game_over = True
                self._display.render_gameboard(self._gameboard.get_gameboard())

if __name__ == "__main__":
    game = Controller()
    game.start_game()