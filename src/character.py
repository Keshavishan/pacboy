class Character():
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.speed = 1
        self.start = x, y
        self.last = None
        self.invulnerable = False
        self.avatar = None

    def update_position(self, x, y) -> None:
        self.x, self.y = x, y
    
    def curr_loc(self) -> tuple:
        return self.x, self.y

    def invulnerability(self) -> None:
        self.invulnerable = not self.invulnerable