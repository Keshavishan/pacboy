from graphics import Graphics


class Dot():
    id = 2
    boostUpId = 3
    
    def __init__(self, x, y, graphics: Graphics, boost = False):
        self.x = x
        self.y = y
        self.boost = boost
        self.avatar = graphics.get('boost' if self.boost else 'pickup')
