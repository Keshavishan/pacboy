from character import Character
from graphics import Graphics

class Pacman():
    id = 1
    def __init__(self, x, y, graphics: Graphics, direction = 'West'):
        Character.__init__(self, x, y, direction)

        self.graphics = graphics
        self.direction_image(graphics)

        self.last_direction, self.next_direction = 'Left', None

    def change_direction(self, direction):
        self.last_direction = self.direction
        self.direction = direction

    def direction_image(self, graphics: Graphics):
        self.avatar = graphics.get(f'pacman_{self.direction[0].lower()}' )

