from ghost import Ghost
from graphics import Graphics

class Inky(Ghost):
    id = 4
    name = 'inky'
    def __init__(self, x, y, graphics: Graphics, direction=None):
        super().__init__(x, y, Inky.name, graphics, direction=direction)

class Blinky(Ghost):
    id = 5
    name = 'blinky'
    def __init__(self, x, y, graphics: Graphics, direction=None):
        super().__init__(x, y, Blinky.name, graphics, direction=direction)

class Pinky(Ghost):
    id = 6
    name = 'pinky'
    def __init__(self, x, y, graphics: Graphics, direction=None):
        super().__init__(x, y, Pinky.name, graphics, direction=direction)

class Clyde(Ghost):
    id = 7
    name = 'clyde'
    def __init__(self, x, y, graphics: Graphics, direction=None):
        super().__init__(x, y, Clyde.name, graphics, direction=direction)

ghosts = [Inky, Blinky, Pinky, Clyde]