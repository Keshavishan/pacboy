from character import Character
from graphics import Graphics

class Ghost(Character):
    def __init__(self, x, y, ghost, graphics: Graphics, mode = "scatter", direction = None):
        Character.__init__(self, x, y, direction)
        self.ghost = ghost
        self.slowed_down = False
        self.i = 0
        self.set_avatar(ghost, graphics)

    def set_avatar(self, ghost, graphics: Graphics):
        if self.invulnerable:
            self.avatar = graphics.get('ghost_vulnerable')
        else:
            self.avatar = graphics.get(ghost)