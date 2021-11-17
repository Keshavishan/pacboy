from character import Character
from graphics import Graphics

class Ghost(Character):
    def __init__(self, x, y, ghost, graphics: Graphics, direction = None):
        Character.__init__(self, x, y, direction)
        self.ghost = ghost
        self.vulnerable = False
        self.slowed_down = False

        self.set_avatar(ghost, graphics)

    def set_avatar(self, ghost, graphics: Graphics):
        if self.vulnerable:
            self.avatar = graphics.get('ghost_vulnerable')
        else:
            self.avatar = graphics.get(ghost)