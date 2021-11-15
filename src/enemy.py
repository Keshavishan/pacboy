from character import Character
from graphics import Graphics

class Enemy(Character):
    inky = (4, 'inky')
    blinky = (5, 'blinky')
    pinky = (6, 'pinky')
    clyde = (7, 'clyde')

    def __init__(self, x, y, enemy, graphics: Graphics, direction = None):
        Character.__init__(self, x, y, direction)
        self.enemies = [Enemy.inky, Enemy.blinky, Enemy.pinky, Enemy.clyde]
        self.enemy = enemy
        self.vulnerable = False
        self.slowed_down = False

        self.set_avatar(enemy, graphics)

    def set_avatar(self, enemy, graphics: Graphics):
        if self.vulnerable:
            self.avatar = graphics.get('vulnerable_ghost')
        else:
            self.avatar = graphics.get([x for x in self.enemies if enemy == x[0]][0][1])