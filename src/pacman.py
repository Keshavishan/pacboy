from character import Character
from dot import Dot
from graphics import Graphics

class Pacman(Character):
    id = 1

    def __init__(self, x, y, graphics: Graphics, direction = 'West'):
        Character.__init__(self, x, y, direction)

        self.graphics = graphics
        self.direction_image(graphics)

        self.last_direction, self.next_direction = 'West', None

    def change_direction(self, direction):
        self.last_direction = self.direction
        self.direction = direction

    def direction_image(self, graphics: Graphics):
        self.avatar = graphics.get(f'pacman_{self.direction[0].lower()}' )

    def curr_location(self):
        return self.y, self.x

    def teleport(self):
        ''' This function controls '''
        if self.direction == 'Left':
            self.update_position(27, 14)
        else:
            self.update_position(0, 14)