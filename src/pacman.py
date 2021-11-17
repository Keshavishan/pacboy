from boost import Boost
from character import Character
from dot import Dot
from graphics import Graphics

class Pacman(Character):
    id = 1
    boostTime = 45

    def __init__(self, x, y, graphics: Graphics, direction = 'West'):
        Character.__init__(self, x, y, direction)
        self.points = 0
        self.lives = 3
        self.level = 1

        self.graphics = graphics
        self.set_avatar(graphics)

        self.last_direction, self.next_direction = 'West', None
        self.boostTime = 45

    def change_direction(self, direction):
        self.last_direction = self.direction
        self.direction = direction

    def set_avatar(self, graphics: Graphics):
        self.avatar = graphics.get(f'pacman_{self.direction[0].lower()}' )

    def curr_location(self):
        return self.y, self.x

    def teleport(self):
        if self.direction == 'West':
            self.update_position(27, 14)
        else:
            self.update_position(0, 14)

    def decrease_boost(self):
        print(self.boostTime)
        self.boostTime -= 1

    def collision(self, collisionWith):
        if type(collisionWith) == Dot:
            self.points += 10
        elif type(collisionWith) == Boost:
            self.points += 50

            if not self.invulnerable:
                self.invulnerable = not self.invulnerable
            else:
                self.boostTime = self.boostTime + Pacman.boostTime