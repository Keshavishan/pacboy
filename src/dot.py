from graphics import Graphics

class Dot():
    id = 2
    
    def __init__(self, x, y, graphics: Graphics):
        self.x = x
        self.y = y
        self.avatar = graphics.get('dot')
