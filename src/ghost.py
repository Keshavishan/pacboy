from character import Character
from graphics import Graphics
from dot import Dot
from powerPellet import PowerPellet
from pacman import Pacman
from collections import deque
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

    # def update_mode(self, count):
    #     if not self.invulnerable:
    #         no_seconds = count % 8
    #         if no_seconds < 8 or no_seconds in range(27, 34) or no_seconds in range(54, 59) or no_seconds in range(79, 84):
    #             self.mode = 1
    #         else:
    #             self.mode = 2
    #     else:
    #         self.mode = 3
    
    def _path_length(self, path) -> int:
        ''' This function is a helper function to avoid index errors depending on
            how large the path is. If the path is larger than 1, we can just get
            the [1] index of the list for the next location. Otherwise, if it is
            only 1, we do [0] since a list of length 1 only has that index value. '''
        if len(path) > 1:
            return 1
        else:
            return 0

    def scatter(self, maze, pacman, count, endpoint_y, endpoint_x):
        start = self.x, self.y

        path = self.bfs(maze, start, endpoint_y, endpoint_x)

        print(path)

        # if path is not None and path != []:
        #     distance = 1 if len(path) else 0

        #     if self.y < path[distance][1]:
        #         self.direction = 'South'

        #     elif self.y > path[distance][1]:
        #         self.direction = 'North'

        #     elif self.x < path[distance][0]:
        #         self.direction = 'East'

        #     elif self.x > path[distance][0]:
        #         self.direction = 'West'

        #     self.last = (self.x, self.y)

        #     self.run()



    def bfs(self, maze: Maze, start, endpoint_y, endpoint_x):
        print(endpoint_y, endpoint_x)
        queue = deque([[start]])
        seen = set([start])
        gamestate = maze.state


        while queue:
            path = queue.popleft()
            x, y = path[-1]

            if (y, x) == (endpoint_y, endpoint_x):
                return path

            for x2, y2 in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                if self.wanted_path_indexes(maze, gamestate, seen, x2, y2):
                    queue.append(path + [(x2, y2)])
                    # print(queue)
                    seen.add((x2, y2))

    def wanted_path_indexes(self, maze: Maze, gamestate, seen, x, y) -> bool:
        ''' To be a wanted index, x and y have to be within the board boundaries.
            The position of y, x on the board also can not be a wall, since we need
            a valid path. And (x, y) can not be duplicated, so must not be in the set seen. '''
        return 0 <= x < maze.m_width and \
               0 <= y < maze.m_height and \
               type(gamestate[y][x]) != Wall and \
               (x, y) not in seen

        