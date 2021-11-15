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
        mapping = [ listmaker(0, 28),
          ([0] + listmaker(4, 12) + [0]) * 2,
          [0, 4, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 4, 0, 0, 4, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 4, 0],
          [0, 3, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 4, 0, 0, 4, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 3, 0],
          [0, 4, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 4, 0, 0, 4, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 4, 0],
          [0] + listmaker(4, 26) + [0],
          [0, 4, 0, 0, 0, 0, 4, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 4, 0, 0, 0, 0, 4, 0],
          [0, 4, 0, 0, 0, 0, 4, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 4, 0, 0, 0, 0, 4, 0],
          [0, 4, 4, 4, 4, 4, 4, 0, 0, 4, 4, 4, 4, 0, 0, 4, 4, 4, 4, 0, 0, 4, 4, 4, 4, 4, 4, 0],
          [0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, None, 0, 0, None, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, None, 0, 0, None, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 4, 0, 0, None, None, None, None, None, None, None, None, None, None, 0, 0, 4, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 4, 0, 0, None, 0, None, 0, 0, 0, 0, None, 0, None, 0, 0, 4, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 4, 0, 0, None, 0, None, None, None, None, None, None, 0, None, 0, 0, 4, 0, 0, 0, 0, 0, 0],
          [None, None, None, None, None, None, 4, 0, 0, None, 0, None, None, None, None, None, None, 0, None, 0, 0, 4, None, None, None, None, None, None],
          [0, 0, 0, 0, 0, 0, 4, 0, 0, None, 0, None, 5, 6, 7, 8, None, 0, None, 0, 0, 4, 0, 0, 0, 0, 0, 0],
          [None, None, None, None, None, 0, 4, 0, 0, None, 0, 0, 0, 0, 0, 0, 0, 0, None, 0, 0, 4, 0, None, None, None, None],
          [None, None, None, None, None, 0, 4, 0, 0, None, None, None, None, None, None, None, None, None, None, 0, 0, 4, 0, None, None, None, None, None],
          [None, None, None, None, None, 0, 4, 0, 0, None, 0, 0, 0, 0, 0, 0, 0, 0, None, 0, 0, 4, 0, None, None, None, None, None],
          [0, 0, 0, 0, 0, 0, 4, 0, 0, None, 0, 0, 0, 0, 0, 0, 0, 0, None, 0, 0, 4, 0, 0, 0, 0, 0, 0],
          ([0] + listmaker(4, 12) + [0]) * 2,
          [0, 4, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 4, 0, 0, 4, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 4, 0],
          [0, 4, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 4, 0, 0, 4, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 4, 0],
          [0, 3, 4, 4, 0, 0, 4, 4, 4, 4, 4, 4, 4, None, 1, 4, 4, 4, 4, 4, 4, 4, 0, 0, 4, 4, 3, 0, 0],
          [0, 0, 0, 4, 0, 0, 4, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 4, 0, 0, 4, 0, 0, 0],
          [0, 0, 0, 4, 0, 0, 4, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 4, 0, 0, 4, 0, 0, 0],
          [0, 4, 4, 4, 4, 4, 4, 0, 0, 4, 4, 4, 4, 0, 0, 4, 4, 4, 4, 0, 0, 4, 4, 4, 4, 4, 4, 0],
          [0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0],
          [0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0],
          [0] + listmaker(4, 26) + [0],
          listmaker(0, 28)]

        self.m_height, self.m_width = len(mapping), len(mapping[0])
        maze = []

        for i in range(len(mapping)):
            row = []
            for j in range(len(mapping[i])):
                if mapping[i][j] == Wall.id:
                    row.append( Wall(j, i) )

                elif mapping[i][j] == Pacman.id:
                    row.append( Pacman(j, i, self.graphics) )

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