from powerPellet import PowerPellet
from dot import Dot
from graphics import Graphics
from helper import listmaker
from pacman import Pacman
from wall import Wall
import ghosts

class Maze():
    def __init__(self, graphics: Graphics):
        self.graphics = graphics
        self.m_width, self.m_height, self.state, self.pacman = None, None, None, None
        self.ghosts, self.objects = set(), set()
        self.game_over = False
        self.update_counter = 0
   
    def new_level(self):
        points, lives, level = self.stats()
        self.ghosts, self.game_objects = set(), set()

        mapping = [ listmaker(0, 28), #0
            ([0] + listmaker(2, 12) + [0]) * 2, #1
            [0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 0],#2
            [0, 3, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 3, 0],#3
            [0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 0],#4
            [0] + listmaker(2, 26) + [0],#5
            [0, 2, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 2, 0],#6
            [0, 2, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 2, 0],#7
            [0, 2, 2, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 2, 2, 0],#8
            [0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, None, 0, 0, None, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0],#9
            [0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, None, 0, 0, None, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0],#10
            [0, 0, 0, 0, 0, 0, 2, 0, 0, None, None, None, None, None, None, None, None, None, None, 0, 0, 2, 0, 0, 0, 0, 0, 0],#11
            [0, 0, 0, 0, 0, 0, 2, 0, 0, None, 0, None, 0, 0, 0, 0, None, 0, None, 0, 0, 2, 0, 0, 0, 0, 0, 0],#12
            [0, 0, 0, 0, 0, 0, 2, 0, 0, None, 0, None, None, None, None, None, None, 0, None, 0, 0, 2, 0, 0, 0, 0, 0, 0],#13
            [None, None, None, None, None, None, 2, 0, 0, None, 0, None, None, None, None, None, None, 0, None, 0, 0, 2, None, None, None, None, None, None],#14
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
                    row.append( Wall(j, i, self.graphics) )

                elif mapping[i][j] == Pacman.id:
                    row.append( Pacman(j, i, self.graphics) )

                elif mapping[i][j] == Dot.id:
                    row.append( Dot(j, i, self.graphics) )

                elif mapping[i][j] == PowerPellet.id:
                    row.append(PowerPellet(j, i, self.graphics))
                
                # elif mapping[i][j] == ghosts.Inky.id:
                #     row.append(ghosts.Inky(j, i, self.graphics))

                elif mapping[i][j] == ghosts.Blinky.id:
                    row.append(ghosts.Blinky(j, i, self.graphics))

                # elif mapping[i][j] == ghosts.Pinky.id:
                #     row.append(ghosts.Pinky(j, i, self.graphics))

                # elif mapping[i][j] == ghosts.Clyde.id:
                #     row.append(ghosts.Clyde(j, i, self.graphics))

                else:
                    row.append(None)

            maze.append(row)
        
        self.state = maze
        self.update_maze()

        self.pacman.points, self.pacman.lives, self.pacman.level = points, lives, level
        self.ghosts = { e for e in self.objects if type(e) in ghosts.ghosts }

        
    def stats(self) -> tuple:
        # Game has already started and is transitioning to a new level
        if self.state is not None:
            return self.pacman.points, self.pacman.lives, self.pacman.level + 1
        else:
            return 0, 3, 1

    def _update_previous_board_square(self, game_object):
        if game_object.last is not None:
            if (game_object.y, game_object.x) != game_object.last:
                previous_y, previous_x = game_object.last

                if type(self.state[previous_y][previous_x]) == None:
                    self.state[previous_y][previous_x] = None

    def update_maze(self):
        self.update_counter += 1

        objects = set()
        for rows in self.state:
            for objs in rows:
                if objs is not None:
                    objects.add(objs)
        
        self.objects = objects

        self.pacman = self.pacman_location()
        y, x = self.pacman.curr_location()
        if (y == 14 and x == 0) or (y == 14 and x == 27):
            self.pacman.teleport()
            self.state[self.pacman.y][self.pacman.x] = self.pacman

        else:
            self.pacman.collision(self.state[y][x])

        if self.pacman.invulnerable:
            if self.pacman.boostTime == Pacman.boostTime:
                for ghost in self.ghosts:
                    ghost.invulnerable = True
                    ghost.set_avatar(ghost.name, self.graphics)
                self.pacman.decrease_boost()

            elif self.pacman.boostTime == 0:
                for ghost in self.ghosts:
                    ghost.invulnerable = False
                    ghost.set_avatar(ghost.name, self.graphics)
                self.pacman.boostTime = Pacman.boostTime
                self.pacman.invulnerable = not self.pacman.invulnerable
            
            else:
                self.pacman.decrease_boost() 

        for ghost in self.ghosts:
            ghost.update_mode(self.update_counter)
            ghost.move(self, self.pacman)
            self._update_previous_board_square(ghost)
            self.state[ghost.y][ghost.x] = ghost

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
            return type(self.state[y + 1][x]) != Wall and (y + 1, x) not in [(13,11), (13,16)]

        elif direction == 'North':
            return type(self.state[y - 1][x]) != Wall

        else:
            return type(self.state[y][x - 1 if direction == "West" else x + 1]) != Wall

    def update_directions(self):
        self.validate_upcoming_movement()

        self.pacman.last = self.pacman.curr_location()

        if self.can_change_direction(self.pacman.direction):
            self.pacman.run()

    def validate_upcoming_movement(self):
        if self.pacman.next_direction is not None:
            if self.can_change_direction(self.pacman.next_direction):
                self.pacman.change_direction(self.pacman.next_direction)
                self.pacman.next_direction = None
                self.pacman.set_avatar(self.graphics)