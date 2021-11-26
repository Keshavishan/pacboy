"""
The character class is used as a base for the characters in the game i.e Pacman and the Ghost (Blinky)
"""


class Character:
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
        """
        Updates the position of the character in the maze
        """
        self.x, self.y = x, y

    def curr_loc(self):
        """
        Returns the current location of the character
        """
        return self.y, self.x

    def run(self):
        """
        Based on the direction the character is facing, run will update the position of the character
        """
        if self.direction == 'North':
            self.y -= self.speed

        elif self.direction == 'East':
            self.x += self.speed

        elif self.direction == 'South':
            self.y += self.speed

        elif self.direction == 'West':
            self.x -= self.speed
