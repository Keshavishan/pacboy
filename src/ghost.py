from character import Character
from graphics import Graphics
from dot import Dot
from powerPellet import PowerPellet
from pacman import Pacman
from collections import deque as queue
from maze import Maze
from wall import Wall

class Ghost(Character):
    def __init__(self, x, y, ghost, graphics: Graphics, mode=1):
        Character.__init__(self, x, y, "North")
        self.ghost = ghost
        self.slowed_down = False
        self.mode = mode
        self.set_avatar(ghost, graphics)

    def set_avatar(self, ghost, graphics: Graphics):
        if self.invulnerable:
            self.avatar = graphics.get('ghost_vulnerable')
        else:
            self.avatar = graphics.get(ghost)

    def update_mode(self, count):
        print("update_mode", self.invulnerable, count)
        if not self.invulnerable:
            no_seconds = (count * 125) / 1000
            if no_seconds < 8 or no_seconds in range(27, 34) or no_seconds in range(54, 59) or no_seconds in range(79, 84):
                self.mode = 1
            else:
                self.mode = 2
        else:
            self.mode = 3
    
    def _path_length(self, path) -> int:
        ''' This function is a helper function to avoid index errors depending on
            how large the path is. If the path is larger than 1, we can just get
            the [1] index of the list for the next location. Otherwise, if it is
            only 1, we do [0] since a list of length 1 only has that index value. '''
        if len(path) > 1:
            return 1
        else:
            return 0

    def scatter(self, maze, pacman, target):
        start = self.x, self.y

        path = self.bfs(maze, start, target)

        self.ghost_move(path, maze, target)

    def ghost_move(self, path, maze, target):
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

            self.last = (self.y, self.x)

            self.run()

        else:
            possible_moves = self.possible_moves(maze)

            quickest_path = self.quickest_path(possible_moves, target)
            self.last = (self.y, self.x)
            self.x, self.y, self.direction = quickest_path
    
    def possible_moves(self, maze):
        possible_moves = []

        def is_valid(object):
            if (type(object) == Dot or object == None or type(object) == PowerPellet) or object.name == self.ghost:
                return True
            return False

        if is_valid(maze.state[self.y - 1][self.x]) and self.direction != "South": # North
            possible_moves.append((self.x, self.y - 1, "North"))
        if is_valid(maze.state[self.y + 1][self.x]) and self.direction != "North": # South
            possible_moves.append((self.x, self.y + 1, "South"))
        if is_valid(maze.state[self.y][self.x + 1]) and self.direction != "West": # East
            possible_moves.append((self.x + 1, self.y, "East"))
        if is_valid(maze.state[self.y][self.x - 1]) and self.direction != "East": # West
            possible_moves.append((self.x - 1, self.y, "West"))
        return possible_moves

    def quickest_path(self, possible_moves, target):
        quickest_path = (1500, None)

        for move in possible_moves:
            distance = (move[0] - target[0]) ** 2 + (move[1] - target[1]) ** 2

            if quickest_path[0] > distance:
                quickest_path = (distance, move)


        return quickest_path[1]



    def bfs(self, maze: Maze, start, target):
        q = queue([[start]])
        visited = set([start])

        while q:
            path = q.popleft()

            x, y = path[-1]

            if (x, y) == target:
                return path

            for x1, y1 in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                if 1 <= x1 < maze.m_width and 1 <= y1 < maze.m_height and type(maze.state[y1][x1]) != Wall and (x1, y1) not in visited and (y1, x1) != self.last:
                    q.append(path + [(x1, y1)])
                    visited.add((x1, y1))

        