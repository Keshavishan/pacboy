from ghost import Ghost
from graphics import Graphics
from pacman import Pacman

class Inky(Ghost):
    id = 4
    name = 'inky'
    target = (27, 27) # x, y

    def __init__(self, x, y, graphics: Graphics):
        super().__init__(x, y, Inky.name, graphics)
        
    def move(self, maze, pacman: Pacman):
        curr_pos = self.x, self.y

    def frightened():
        pass

    def chase():
        pass

class Blinky(Ghost):
    id = 5
    name = 'blinky'
    target = (27, 0) # x, y

    def __init__(self, x, y, graphics: Graphics):
        super().__init__(x, y, Blinky.name, graphics)
    
    def move(self, maze, pacman: Pacman):
        curr_pos = self.x, self.y

        if self.mode == 1:
            self.scatter(maze, curr_pos, Blinky.target)
        elif self.mode == 2:
            self.chase()

    def frightened(self):
        pass

    def chase(self):
        pass

class Pinky(Ghost):
    id = 6
    name = 'pinky'
    target = (0, 0) # x, y

    def __init__(self, x, y, graphics: Graphics):
        super().__init__(x, y, Pinky.name, graphics)

    def move(self, maze, pacman: Pacman):
        curr_pos = self.x, self.y

        if self.mode == 1:
            self.scatter(maze, curr_pos, Pinky.target)
        elif self.mode == 2:
            self.chase()

    def frightened(self):
        pass

    def chase(self):
        pass

class Clyde(Ghost):
    id = 7
    name = 'clyde'
    target = (0, 27) # x, y

    def __init__(self, x, y, graphics: Graphics):
        print("clyde", x, y)
        super().__init__(x, y, Clyde.name, graphics)

    def move(self, maze, pacman: Pacman):
        self.i += 1
        curr_pos = self.x, self.y

        if self.mode == 1:
            self.scatter(maze, curr_pos, Clyde.target)
        elif self.mode == 2:
            self.chase()

    def frightened(self):
        pass

    def chase(self):
        pass



ghosts = [Inky, Blinky, Pinky, Clyde]