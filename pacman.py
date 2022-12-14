"""
This class creates and handles the updating of Pacman's state including the number of points and lives he has as well as
what level he's at.
"""
from powerPellet import PowerPellet
from character import Character
from pellet import Pellet
from graphics import Graphics
import ghost


class Pacman(Character):
    id = 1
    name = "pacman"

    def __init__(self, x, y, graphics: Graphics, saved_game={}, direction='West'):
        Character.__init__(self, x, y, direction)
        self.points = 0
        self.lives = 3
        self.level = 1

        self.graphics = graphics
        

        self.last_direction, self.next_direction = 'West', None
        self.defBoostTime = 45
        self.boostTime = 45
        self.ghosts_eaten = 0

        self.invincible = False

        self.is_respawning = False
        self.death = False

        self.double_points = False

        for key in saved_game:
            setattr(self, key, saved_game[key])
        
        self.set_avatar(graphics)


    def change_direction(self, direction):
        self.last_direction = self.direction
        self.direction = direction

    def set_avatar(self, graphics: Graphics):
        self.avatar = graphics.get(f'pacman_{self.direction[0].lower()}')

    def teleport(self):
        if self.direction == 'West':
            self.update_position(27, 14)
        else:
            self.update_position(0, 14)

    def collision(self, collision_with):
        if type(collision_with) == Pellet:
            self.points += Pellet.value * 2 if self.double_points else Pellet.value
        elif type(collision_with) == PowerPellet:
            self.points += PowerPellet.value * 2 if self.double_points else PowerPellet.value

            if not self.invulnerable:
                self.invulnerable = not self.invulnerable
            else:
                self.boostTime = self.boostTime + self.defBoostTime

        elif type(collision_with) == ghost.Ghost:
            if self.invulnerable:
                self.ghosts_eaten += 1
                self.points += (100 * self.ghosts_eaten)
            else:
                self.death = True
