from ghost import Ghost
from graphics import Graphics
# from pacman import Pacman

class Inky(Ghost):
    id = 4
    name = 'inky'
    target = (26, 28) # x, y

    def __init__(self, x, y, graphics: Graphics):
        super().__init__(x, y, Inky.name, graphics)

    def move(self, maze, pacman, count):
        # if not self.invulnerable:
        #     if self.mode == 1:
        self.scatter(maze, pacman, count, self.target)

class Blinky(Ghost):
    id = 5
    name = 'blinky'
    target = (26, 2) # x, y

    def __init__(self, x, y, graphics: Graphics):
        super().__init__(x, y, Blinky.name, graphics)

    def move(self, maze, pacman, count):
        print(maze.m_width, maze.m_height)
        self.scatter(maze, pacman, count, self.target)

class Pinky(Ghost):
    id = 6
    name = 'pinky'
    target = (1, 2) # x, y

    def __init__(self, x, y, graphics: Graphics):
        super().__init__(x, y, Pinky.name, graphics)

    def move(self, maze, pacman, count):
        self.scatter(maze, pacman, count, self.target)

class Clyde(Ghost):
    id = 7
    name = 'clyde'
    target = (1, 28) # x, y

    def __init__(self, x, y, graphics: Graphics):
        super().__init__(x, y, Clyde.name, graphics)

    def move(self, maze, pacman, count):
        self.scatter(maze, pacman, count, self.target)



ghosts = [Inky, Blinky, Pinky, Clyde]