from character import Character
from graphics import Graphics
from pacman import Pacman
from collections import deque as queue
from wall import Wall

class Ghost(Character):
    id = 4
    name = 'blinky'

    def __init__(self, x, y, graphics: Graphics):
        Character.__init__(self, x, y, "North")
        self.set_avatar(Ghost.name, graphics)
        self.pellet = None

    def set_avatar(self, ghost, graphics: Graphics):
        if self.invulnerable:
            self.avatar = graphics.get('ghost_vulnerable')
        else:
            self.avatar = graphics.get(ghost)

    def move(self, maze, pacman: Pacman):
        self.make_move(maze, pacman)

    def make_move(self, maze, pacman: Pacman):
        start = (self.x, self.y)
        
        target = (self.start[1], self.start[0]) if self.invulnerable else pacman.curr_loc()
        path = self.shortest_path(maze, start, target)

        if path:
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
        q = queue([[start]])
        seen = set([start])

        while q:
            path = q.popleft()
            x, y = path[-1]

            if (y, x) == target:
                return path

            adjacent_squares = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]

            for x1, y1 in adjacent_squares:
                if 0 <= x1 < maze.m_width and 0 <= y1 < maze.m_height and type(maze.state[y1][x1]) != Wall and (x1, y1) not in seen and (y1, x1) != self.last:
                    q.append(path + [(x1, y1)])
                    seen.add((x1, y1))
    


        