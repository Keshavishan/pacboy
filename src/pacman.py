from powerPellet import PowerPellet
from character import Character
from pellet import Pellet
from graphics import Graphics
import ghost

class Pacman(Character):
    id = 1
    name = "pacman"

    def __init__(self, x, y, graphics: Graphics, direction = 'West'):
        Character.__init__(self, x, y, direction)
        self.points = 0
        self.lives = 3
        self.level = 1

        self.graphics = graphics
        self.set_avatar(graphics)

        self.last_direction, self.next_direction = 'West', None
        self.defBoostTime = 45
        self.boostTime = 45
        self.ghosts_eaten = 0

        self.is_respawning = False
        self.death = False

    def change_direction(self, direction):
        self.last_direction = self.direction
        self.direction = direction

    def set_avatar(self, graphics: Graphics):
        self.avatar = graphics.get(f'pacman_{self.direction[0].lower()}' )

    def teleport(self):
        if self.direction == 'West':
            self.update_position(27, 14)
        else:
            self.update_position(0, 14)

    def decrease_boost(self):
        self.boostTime -= 1

    def collision(self, collisionWith):
        if type(collisionWith) == Pellet:
            self.points += Pellet.value
        elif type(collisionWith) == PowerPellet:
            self.points += PowerPellet.value

            if not self.invulnerable:
                self.invulnerable = not self.invulnerable
            else:
                self.boostTime = self.boostTime + self.defBoostTime

        elif type(collisionWith) in [ghost.Ghost]:
            if not self.invulnerable:
                self.ghosts_eaten += 1
                self.points += (100 * self.ghosts_eaten)
            else:
                self.death = True