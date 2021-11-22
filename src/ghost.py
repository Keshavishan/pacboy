import random
from character import Character
from graphics import Graphics
from dot import Dot
from powerPellet import PowerPellet
from pacman import Pacman


class Ghost(Character):
    def __init__(self, x, y, ghost, graphics: Graphics, mode=1):
        Character.__init__(self, x, y, "North")
        self.ghost = ghost
        self.slowed_down = False
        self.i = 0
        self.mode = mode
        self.set_avatar(ghost, graphics)

    def set_avatar(self, ghost, graphics: Graphics):
        if self.invulnerable:
            self.avatar = graphics.get('ghost_vulnerable')
        else:
            self.avatar = graphics.get(ghost)

    def update_mode(self):
        self.i += 1
        if not self.invulnerable:
            no_seconds = self.i % 8
            if no_seconds < 8 or no_seconds in range(27, 34) or no_seconds in range(54, 59) or no_seconds in range(79, 84):
                self.mode = 1
            else:
                self.mode = 2
        else:
            self.mode = 3

    def possible_moves(self, maze):
        possible_moves = []

        def is_valid(object):
            if (type(object) == Dot or object == None or type(object) == PowerPellet or type(object) == Pacman):
                return True
            return False
        if is_valid(maze[self.y][self.x + 1]) and self.last != (self.y, self.x + 1): # East
            possible_moves.append((self.x + 1, self.y, "East"))
        if is_valid(maze[self.y + 1][self.x]) and self.last != (self.y + 1, self.x): # South
            possible_moves.append((self.x, self.y + 1, "South"))
        if is_valid(maze[self.y][self.x - 1]) and self.last != (self.y, self.x - 1): # West
            possible_moves.append((self.x - 1, self.y, "West"))
        if is_valid(maze[self.y - 1][self.x]) and self.last != (self.y - 1, self.x): # North
            possible_moves.append((self.x, self.y - 1, "North"))
        return possible_moves

    def move(self, maze, target): 
        possible_moves = self.possible_moves(maze)
        choice = random.choice(possible_moves)

        self.x, self.y, self.direction = choice
        