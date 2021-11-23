from character import Character
from graphics import Graphics
from pellet import Pellet
from powerPellet import PowerPellet
from pacman import Pacman
from collections import deque as queue
from maze import Maze
from wall import Wall

class Ghost(Character):
    def __init__(self, x, y, ghost, graphics: Graphics, mode=1):
        Character.__init__(self, x, y, "North")
        self.ghost = ghost
        self.slowed_down = False
        self.mode = mode
        self.set_avatar(ghost, graphics)
        self.pellet = None

    def set_avatar(self, ghost, graphics: Graphics):
        if self.invulnerable:
            self.avatar = graphics.get('ghost_vulnerable')
        else:
            self.avatar = graphics.get(ghost)

    def update_mode(self, count):
        if not self.invulnerable:
            no_seconds = (count * 125) / 1000
            if no_seconds < 2 or no_seconds in range(27, 34) or no_seconds in range(54, 59) or no_seconds in range(79, 84):
                self.mode = 1
            else:
                self.mode = 2
        else:
            self.mode = 3
    


        