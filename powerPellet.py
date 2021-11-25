from graphics import Graphics

class PowerPellet():
    id = 3
    name = "powerPellet"
    value = 50

    def __init__(self, x, y, graphics: Graphics):
        self.x = x
        self.y = y
        self.avatar = graphics.get('powerPellet')
