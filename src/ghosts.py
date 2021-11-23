from ghost import Ghost
from graphics import Graphics
# from pacman import Pacman
from collections import deque
from pacman import Pacman

from wall import Wall

class Inky(Ghost):
    id = 4
    name = 'inky'
    target = (26, 28) # x, y

    def __init__(self, x, y, graphics: Graphics):
        super().__init__(x, y, Inky.name, graphics)

    def move(self, maze, pacman):
        # if not self.invulnerable:
        #     if self.mode == 1:
        #         self.scatter(maze, self.target)

        #     elif self.mode == 2:
        #         self.chase()
        pass


    def chase(self):
        print()

class Blinky(Ghost):
    id = 5
    name = 'blinky'
    target = (26, 2) # x, y

    def __init__(self, x, y, graphics: Graphics):
        super().__init__(x, y, Blinky.name, graphics)

    def move(self, maze, pacman):
        if not self.invulnerable:
            self.chase(maze, pacman)

    def chase(self, maze, pacman: Pacman):
        start = self.x, self.y
        self.make_move(maze, start, pacman)

    def make_move(self, maze, start, pacman: Pacman):
        if self.invulnerable:
            path = self.bfs(maze, start, (self.start[1], self.start[0]))[:-1]
        else:
            path = self.bfs(maze, start, (pacman.y, pacman.x))

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

    def bfs(self, maze, start, target):
        queue = deque([[start]])
        seen = set([start])

        while queue:
            path = queue.popleft()
            x, y = path[-1]

            if (y, x) == target:
                return path

            adjacent_squares = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]

            for x1, y1 in adjacent_squares:
                if 0 <= x1 < maze.m_width and 0 <= y1 < maze.m_height and type(maze.state[y1][x1]) != Wall and (x1, y1) not in seen:
                    queue.append(path + [(x1, y1)])
                    seen.add((x1, y1))


class Pinky(Ghost):
    id = 6
    name = 'pinky'
    target = (1, 2) # x, y

    def __init__(self, x, y, graphics: Graphics):
        super().__init__(x, y, Pinky.name, graphics)

    def move(self, maze, pacman):
        # if not self.invulnerable:
        #     if self.mode == 1:
        #         self.scatter(maze, self.target)

        #     elif self.mode == 2:
        #         self.chase()
        pass

    def chase(self):
        print()

class Clyde(Ghost):
    id = 7
    name = 'clyde'
    target = (1, 28) # x, y

    def __init__(self, x, y, graphics: Graphics):
        super().__init__(x, y, Clyde.name, graphics)

    def move(self, maze, pacman):
         # if not self.invulnerable:
        #     if self.mode == 1:
        #         self.scatter(maze, self.target)

        #     elif self.mode == 2:
        #         self.chase()
        pass


    def chase(self):
        print()



ghosts = [Inky, Blinky, Pinky, Clyde]