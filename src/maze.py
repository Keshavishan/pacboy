from boost import Boost
from dot import Dot
from enemy import Enemy
from graphics import Graphics
from helper import listmaker
from pacman import Pacman
from wall import Wall

class Maze():
    restricted_area = [(13,11), (13,16)]

    def __init__(self, graphics: Graphics):
        self.graphics = graphics
        self.m_width, self.m_height, self.state, self.pacman = None, None, None, None
        self.enemies, self.objects  = set(), set()
        self.game_over = False

    def new_level(self):
        mapping = mapping = [ listmaker(0, 28),
            ([0] + listmaker(2, 12) + [0]) * 2,
            [0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 0],
            [0, 3, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 3, 0],
            [0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 0],
            [0] + listmaker(2, 26) + [0],
            [0, 2, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 2, 0],
            [0, 2, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 2, 0],
            [0, 2, 2, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 2, 2, 0],
            [0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, None, 0, 0, None, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, None, 0, 0, None, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 2, 0, 0, None, None, None, None, None, None, None, None, None, None, 0, 0, 2, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 2, 0, 0, None, 0, None, 0, 0, 0, 0, None, 0, None, 0, 0, 2, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 2, 0, 0, None, 0, None, None, None, None, None, None, 0, None, 0, 0, 2, 0, 0, 0, 0, 0, 0],
            [None, None, None, None, None, None, 2, 0, 0, None, 0, None, None, None, None, None, None, 0, None, 0, 0, 2, None, None, None, None, None, None],
            [0, 0, 0, 0, 0, 0, 2, 0, 0, None, 0, None, 4, 5, 6, 7, None, 0, None, 0, 0, 2, 0, 0, 0, 0, 0, 0],
            [None, None, None, None, None, 0, 2, 0, 0, None, 0, 0, 0, 0, 0, 0, 0, 0, None, 0, 0, 2, 0, None, None, None, None],
            [None, None, None, None, None, 0, 2, 0, 0, None, None, None, None, None, None, None, None, None, None, 0, 0, 2, 0, None, None, None, None, None],
            [None, None, None, None, None, 0, 2, 0, 0, None, 0, 0, 0, 0, 0, 0, 0, 0, None, 0, 0, 2, 0, None, None, None, None, None],
            [0, 0, 0, 0, 0, 0, 2, 0, 0, None, 0, 0, 0, 0, 0, 0, 0, 0, None, 0, 0, 2, 0, 0, 0, 0, 0, 0],
            ([0] + listmaker(2, 12) + [0]) * 2,
            [0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 0],
            [0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 0],
            [0, 3, 2, 2, 0, 0, 2, 2, 2, 2, 2, 2, 2, None, 1, 2, 2, 2, 2, 2, 2, 2, 0, 0, 2, 2, 3, 0, 0],
            [0, 0, 0, 2, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 2, 0, 0, 0],
            [0, 0, 0, 2, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 2, 0, 0, 0],
            [0, 2, 2, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 2, 2, 0],
            [0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0],
            [0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0],
            [0] + listmaker(2, 26) + [0],
            listmaker(0, 28)
        ]

        self.m_height, self.m_width = len(mapping), len(mapping[0])
        maze = []

        for i in range(len(mapping)):
            row = []
            for j in range(len(mapping[i])):
                if mapping[i][j] == Wall.id:
                    row.append( Wall(j, i) )

                elif mapping[i][j] == Pacman.id:
                    row.append( Pacman(j, i, self.graphics) )

                elif mapping[i][j] == Dot.id:
                    row.append( Dot(j, i, self.graphics) )

                elif mapping[i][j] == Boost.id:
                    row.append(Boost(j, i, self.graphics))
                
                elif mapping[i][j] == Enemy.inky[0] or mapping[i][j] == Enemy.blinky[0] or mapping[i][j] == Enemy.pinky[0] or mapping[i][j] == Enemy.clyde[0]:
                    row.append(Enemy(j, i, mapping[i][j], self.graphics))
                else:
                    row.append(None)

            maze.append(row)

        self.state = maze

        self.update_maze()

    def _update_previous_board_square(self, game_object):
        ''' Updates the previous board square that the game object was in. This only occurs after
            the game object has actually moved ( meaning after first update ). This function avoids
            there being multiple duplicates of the game object on the board, since it replaces the
            last location with None. '''
        if game_object.last is not None:
            if (game_object.y, game_object.x) != game_object.last:
                previous_y, previous_x = game_object.last

                if type(self.state[previous_y][previous_x]) == None:
                    self.state[previous_y][previous_x] = None

    def update_maze(self):
        for rows in self.state:
            for objs in rows:
                if objs != None:
                    self.objects.add(objs)

        self.pacman = self.pacman_location()

        y, x = self.pacman.curr_location()
        if (y == 14 and x == 0) or (y == 14 and x == 27):
            self.pacman.teleport()
            self.state[self.pacman.y][self.pacman.x] = self.pacman

        else:
            self.pacman.contact(self.state[y][x])

        if not self.game_over:
            self._update_previous_board_square(self.pacman)
            self.state[y][x] = self.pacman

        else:
            self.state[y][x] = None

    def pacman_location(self) -> Pacman:
        for obj in self.objects:
            if type(obj) == Pacman:
                return obj
    
    def can_change_direction(self, direction):
        y, x = self.pacman.curr_location()

        if direction == 'South':
            return type(self.state[y + 1][x]) != Wall and (y + 1, x) not in Maze.restricted_area

        elif direction == 'North':
            return type(self.state[y - 1][x]) != Wall

        else:
            return type(self.state[y][x - 1 if direction == "West" else x + 1]) != Wall

    def update_directions(self):
        self.pacman.last = self.pacman.curr_location()

        if self.can_change_direction(self.pacman.direction):
            self.pacman.run()