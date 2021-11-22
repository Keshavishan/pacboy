from ghost import Ghost
from graphics import Graphics
from pacman import Pacman

class Inky(Ghost):
    id = 4
    name = 'inky'
    target = (27, 27) # x, y

    def __init__(self, x, y, graphics: Graphics):
        super().__init__(x, y, Inky.name, graphics)

class Blinky(Ghost):
    id = 5
    name = 'blinky'
    target = (27, 0) # x, y

    def __init__(self, x, y, graphics: Graphics):
        super().__init__(x, y, Blinky.name, graphics)

class Pinky(Ghost):
    id = 6
    name = 'pinky'
    target = (0, 0) # x, y

    def __init__(self, x, y, graphics: Graphics):
        super().__init__(x, y, Pinky.name, graphics)

class Clyde(Ghost):
    id = 7
    name = 'clyde'
    target = (0, 27) # x, y

    def __init__(self, x, y, graphics: Graphics):
        super().__init__(x, y, Clyde.name, graphics)



ghosts = [Inky, Blinky, Pinky, Clyde]