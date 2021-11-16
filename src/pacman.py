from character import Character
from dot import Dot
from graphics import Graphics

class Pacman(Character):
    id = 1

    def __init__(self, x, y, graphics: Graphics, direction = 'West'):
        Character.__init__(self, x, y, direction)
        self.score = 0
        self.life_score = 0
        self.lives = 3
        self.level = 1

        self.graphics = graphics
        self.image(graphics)

        self.last_direction, self.next_direction = 'West', None

    def change_direction(self, direction):
        self.last_direction = self.direction
        self.direction = direction

    def image(self, graphics: Graphics):
        self.avatar = graphics.get(f'pacman_{self.direction[0].lower()}' )

    def curr_location(self):
        return self.y, self.x

    def teleport(self):
        if self.direction == 'West':
            self.update_position(27, 14)
        else:
            self.update_position(0, 14)

    def contact(self, gameObj):
        if type(gameObj) == Dot:
            # if gameObj.boost:
            #     self.score += 50
            #     self.boost_picked_up()
        
            # else:
            self.score += 10