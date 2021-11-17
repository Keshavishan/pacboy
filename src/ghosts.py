from ghost import Ghost
from graphics import Graphics

class Inky(Ghost):
    id = 4
    def __init__(self, x, y, graphics: Graphics, direction=None):
        super().__init__(x, y, 'inky', graphics, direction=direction)

class Blinky(Ghost):
    id = 5
    def __init__(self, x, y, graphics: Graphics, direction=None):
        super().__init__(x, y, 'blinky', graphics, direction=direction)

class Pinky(Ghost):
    id = 6
    def __init__(self, x, y, graphics: Graphics, direction=None):
        super().__init__(x, y, 'pinky', graphics, direction=direction)

class Clyde(Ghost):
    id = 7
    def __init__(self, x, y, graphics: Graphics, direction=None):
        super().__init__(x, y, 'clyde', graphics, direction=direction)