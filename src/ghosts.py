from ghost import Ghost
from graphics import Graphics
# from pacman import Pacman

class Inky(Ghost):
    id = 4
    name = 'inky'
    target = (26, 29) # x, y

    def __init__(self, x, y, graphics: Graphics):
        super().__init__(x, y, Inky.name, graphics)

    def move(self, maze, pacman, count):
        # if not self.invulnerable:
        #     if self.mode == 1:
        self.scatter(maze, pacman, count, self.target[1], self.target[0])

class Blinky(Ghost):
    id = 5
    name = 'blinky'
    target = (26, 1) # x, y

    def __init__(self, x, y, graphics: Graphics):
        super().__init__(x, y, Blinky.name, graphics)

    def move(self, maze, pacman, count):
        print(maze.m_width, maze.m_height)
        self.scatter(maze, pacman, count, self.target[1], self.target[0])

class Pinky(Ghost):
    id = 6
    name = 'pinky'
    target = (1, 1) # x, y

    def __init__(self, x, y, graphics: Graphics):
        super().__init__(x, y, Pinky.name, graphics)

    def move(self, maze, pacman, count):
        self.scatter(maze, pacman, count, self.target[1], self.target[0])

class Clyde(Ghost):
    id = 7
    name = 'clyde'
    target = (1, 29) # x, y

    def __init__(self, x, y, graphics: Graphics):
        super().__init__(x, y, Clyde.name, graphics)

    def move(self, maze, pacman, count):
        self.scatter(maze, pacman, count, self.target[1], self.target[0])



ghosts = [Inky, Blinky, Pinky, Clyde]