from ghost import Ghost
from graphics import Graphics
# from pacman import Pacman

class Inky(Ghost):
    id = 4
    name = 'inky'
    target = (26, 28) # x, y

    def __init__(self, x, y, graphics: Graphics):
        super().__init__(x, y, Inky.name, graphics)

    def move(self, maze, pacman):
        if not self.invulnerable:
            if self.mode == 1:
                self.scatter(maze, pacman, self.target)

            elif self.mode == 2:
                self.chase()

    def chase(self):
        print()

class Blinky(Ghost):
    id = 5
    name = 'blinky'
    target = (26, 2) # x, y

    def __init__(self, x, y, graphics: Graphics):
        super().__init__(x, y, Blinky.name, graphics)

    def move(self, maze, pacman):
        if not self.invulnerable:
            if self.mode == 1:
                self.scatter(maze, pacman, self.target)

            elif self.mode == 2:
                self.chase(maze, pacman)

    def chase(self, maze, pacman):
        start = self.x, self.y
        target = (pacman.x, pacman.y)
        path = self.bfs(maze, start, target)

        self.ghost_move(path, maze, target)

class Pinky(Ghost):
    id = 6
    name = 'pinky'
    target = (1, 2) # x, y

    def __init__(self, x, y, graphics: Graphics):
        super().__init__(x, y, Pinky.name, graphics)

    def move(self, maze, pacman):
        if not self.invulnerable:
            if self.mode == 1:
                self.scatter(maze, pacman, self.target)

            elif self.mode == 2:
                self.chase()

    def chase(self):
        print()

class Clyde(Ghost):
    id = 7
    name = 'clyde'
    target = (1, 28) # x, y

    def __init__(self, x, y, graphics: Graphics):
        super().__init__(x, y, Clyde.name, graphics)

    def move(self, maze, pacman):
        if not self.invulnerable:
            if self.mode == 1:
                self.scatter(maze, pacman, self.target)

            elif self.mode == 2:
                self.chase()

    def chase(self):
        print()



ghosts = [Inky, Blinky, Pinky, Clyde]