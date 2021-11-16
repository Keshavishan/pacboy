from character import Character
from graphics import Graphics

class Enemy(Character):
    def __init__(self, x, y, enemy, graphics: Graphics, direction = None):
        Character.__init__(self, x, y, direction)
        self.enemy = enemy
        self.vulnerable = False
        self.slowed_down = False

        self.set_avatar(enemy, graphics)

    def set_avatar(self, enemy, graphics: Graphics):
        if self.vulnerable:
            self.avatar = graphics.get('vulnerable_ghost')
        else:
            self.avatar = graphics.get(enemy)