from graphics import Graphics

class Pellet():
    id = 2
    name = "pellet"
    
    def __init__(self, x, y, graphics: Graphics):
        self.x = x
        self.y = y
        self.avatar = graphics.get('pellet')
