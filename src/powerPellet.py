from graphics import Graphics

class PowerPellet():
    id = 3
    
    def __init__(self, x, y, graphics: Graphics):
        self.x = x
        self.y = y
        self.avatar = graphics.get('boost')
