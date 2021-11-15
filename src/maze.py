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

                elif mapping[i][j] == Dot.boostUpId:
                    row.append( Dot(j, i, self.graphics, True) )
                
                elif mapping[i][j] == Enemy.inky[0] or mapping[i][j] == Enemy.blinky[0] or mapping[i][j] == Enemy.pinky[0] or mapping[i][j] == Enemy.clyde[0]:
                    row.append( Enemy(j, i, mapping[i][j], self.graphics) )

                else:
                    row.append( None )

            maze.append(row)

        self.state = maze

        self.update_maze()

    def update_maze(self):
        for rows in self.state:
            for objs in rows:
                if objs != None:
                    self.objects.add(objs)