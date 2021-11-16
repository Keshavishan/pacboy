from enemy import Enemy
from graphics import Graphics

class Inky(Enemy):
    id = 4
    def __init__(self, x, y, graphics: Graphics, direction=None):
        super().__init__(x, y, 'inky', graphics, direction=direction)

class Blinky(Enemy):
    id = 5
    def __init__(self, x, y, graphics: Graphics, direction=None):
        super().__init__(x, y, 'blinky', graphics, direction=direction)

class Pinky(Enemy):
    id = 6
    def __init__(self, x, y, graphics: Graphics, direction=None):
        super().__init__(x, y, 'pinky', graphics, direction=direction)

class Clyde(Enemy):
    id = 7
    def __init__(self, x, y, graphics: Graphics, direction=None):
        super().__init__(x, y, 'clyde', graphics, direction=direction)