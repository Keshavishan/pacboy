from ghost import Ghost
from graphics import Graphics
from collections import deque
from pacman import Pacman
from wall import Wall

class Blinky(Ghost):
    id = 4
    name = 'blinky'
    target = (26, 2) # x, y

    def __init__(self, x, y, graphics: Graphics):
        super().__init__(x, y, Blinky.name, graphics)

    # def move(self, maze, pacman):
        # if not self.invulnerable:
            # self.chase(maze, pacman)
        # else:
        #     pass
            # when enemy's can be eaten 

    def move(self, maze, pacman: Pacman):
        self.make_move(maze, pacman)

    def make_move(self, maze, pacman: Pacman):
        start = (self.x, self.y)
        
        target = (self.start[1], self.start[0]) if self.invulnerable else pacman.curr_loc()
        path = self.shortest_path(maze, start, target)

        if self.invulnerable:
            path = path[:-1]

        if path is not None and path != []:
            distance = 1 if len(path) > 1 else 0

            if self.y < path[distance][1]:
                self.direction = 'South'

            elif self.y > path[distance][1]:
                self.direction = 'North'

            elif self.x < path[distance][0]:
                self.direction = 'East'

            elif self.x > path[distance][0]:
                self.direction = 'West'

            self.last = self.curr_loc()
            self.run()

    def shortest_path(self, maze, start, target):
        queue = deque([[start]])
        seen = set([start])

        while queue:
            path = queue.popleft()
            x, y = path[-1]

            if (y, x) == target:
                return path

            adjacent_squares = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]

            for x1, y1 in adjacent_squares:
                if 0 <= x1 < maze.m_width and 0 <= y1 < maze.m_height and type(maze.state[y1][x1]) != Wall and (x1, y1) not in seen and (y1, x1) != self.last:
                    queue.append(path + [(x1, y1)])
                    seen.add((x1, y1))

all_ghosts = [Blinky]