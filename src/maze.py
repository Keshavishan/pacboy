from powerPellet import PowerPellet
from pellet import Pellet
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
            [None, None, None, None, None, None, 2, None, None, None, 0, None, None, None, None, None, None, 0, None, None, None, 2, None, None, None, None, None, None],#14
            [0, 0, 0, 0, 0, 0, 2, 0, 0, None, 0, None, 4, 5, 6, 7, None, 0, None, 0, 0, 2, 0, 0, 0, 0, 0, 0],#15
            [None, None, None, None, None, 0, 2, 0, 0, None, 0, 0, 0, 0, 0, 0, 0, 0, None, 0, 0, 2, 0, None, None, None, None],#16
            [None, None, None, None, None, 0, 2, 0, 0, None, None, None, None, None, None, None, None, None, None, 0, 0, 2, 0, None, None, None, None, None],#17
            [None, None, None, None, None, 0, 2, 0, 0, None, 0, 0, 0, 0, 0, 0, 0, 0, None, 0, 0, 2, 0, None, None, None, None, None],#18
            [0, 0, 0, 0, 0, 0, 2, 0, 0, None, 0, 0, 0, 0, 0, 0, 0, 0, None, 0, 0, 2, 0, 0, 0, 0, 0, 0],#19
            ([0] + listmaker(2, 12) + [0]) * 2,#20
            [0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 0],#21
            [0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 0],#22
            [0, 3, 2, 2, 0, 0, 2, 2, 2, 2, 2, 2, 2, None, 1, 2, 2, 2, 2, 2, 2, 2, 0, 0, 2, 2, 3, 0, 0],#23
            [0, 0, 0, 2, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 2, 0, 0, 0],#24
            [0, 0, 0, 2, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 2, 0, 0, 0],#25
            [0, 2, 2, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 2, 2, 0],#26
            [0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0],#27
            [0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0],#28
            [0] + listmaker(2, 26) + [0],#29
            listmaker(0, 28)#30
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

                elif mapping[i][j] == Pellet.id:
                    row.append( Pellet(j, i, self.graphics) )

                elif mapping[i][j] == PowerPellet.id:
                    row.append(PowerPellet(j, i, self.graphics))
                
                elif mapping[i][j] == ghosts.Blinky.id:
                    row.append(ghosts.Blinky(j, i, self.graphics))
                else:
                    row.append(None)

            maze.append(row)
        
        self.state = maze
        self.update_maze()

        self.pacman.points, self.pacman.lives, self.pacman.level = points, lives, level
        self.ghosts = { e for e in self.objects if type(e) in ghosts.all_ghosts }

    def stats(self) -> tuple:
        if self.state is not None:
            return self.pacman.points, self.pacman.lives, self.pacman.level + 1
        else:
            return 0, 3, 1

    def reset_last_square(self, game_object):
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
                    if type(objs) == Pacman:
                        self.pacman = objs
        
        self.objects = objects

        # while not self.pacman:
        #     self.pacman = self.pacman_location()

        self._update_gamestate()
    
    def _update_gamestate(self):
        ''' Updates the entire gamestate each time it is called. This function is in charge of
            all the character object's movement, and game states as the game progresses. '''
        y, x = self.pacman.curr_loc()
        # Pacman location
        if (y == 14 and x == 0) or (y == 14 and x == 27):
            self.pacman.teleport()
            self.state[self.pacman.y][self.pacman.y] = self.pacman
        else:
            self.pacman.collision(self.state[y][x])                        
        # Pacman boost       
        if self.pacman.invulnerable:
            if self.pacman.boostTime == Pacman.boostTime:
                for ghost in self.ghosts:
                    ghost.invulnerable = True
                    ghost.set_avatar(ghost.name, self.graphics)
                self.pacman.boostTime -= 1

            elif self.pacman.boostTime == 0:
                for ghost in self.ghosts:
                    ghost.invulnerable = False
                    ghost.set_avatar(ghost.name, self.graphics)
                self.pacman.boostTime = Pacman.boostTime
                self.pacman.invulnerable = not self.pacman.invulnerable
            
            else:
                self.pacman.boostTime -= 1
        if self.update_counter % 2 or self.pacman.level > 1:
            for ghost in self.ghosts:
                ghost.move(self, self.pacman)
                self.reset_last_square(ghost)

                if (ghost.y, ghost.x) == (y, x):
                    if not ghost.invulnerable:
                        self.lose_life_update_game()
                    else:
                        self.pacman.collision(ghost)
                        
                else:
                    self.ghost_restore_last_square(ghost)
                    if type(self.state[ghost.y][ghost.x]) in [Pellet, PowerPellet]:
                        ghost.pellet = self.state[ghost.y][ghost.x]
                        
                    self.state[ghost.y][ghost.x] = ghost                         
        # Other
        if self._validate_upcoming_enemy(x):
            if not self.pacman.invulnerable:
                self.lose_life_update_game()

        elif not self.game_over:
            self.reset_last_square(self.pacman)
            self.state[y][x] = self.pacman

        else:
            self.state[y][x] = None

    def _validate_upcoming_enemy(self, x) -> bool:
        if x != self.m_width - 1 and x != 0:
            return self._validate_past_enemy()
    
    def _validate_past_enemy(self):
        if self.pacman.last:
            dy, dx = self.pacman.last
            return type(self.state[dy][dx]) in ghosts.all_ghosts

    def lose_life_update_game(self):
        self.pacman.lives -= 1
        if self.pacman.lives:
            self.return_to_inital_pos()
        else:
            self.game_over = True

    def return_to_inital_pos(self):
        maze = []
        for i in range(len(self.state)):
            row = []
            for j in range(len(self.state[i])):
                if type(self.state[i][j]) == Pacman:
                    row.append(None)
                elif type(self.state[i][j]) in ghosts.all_ghosts:
                    if self.state[i][j].pellet is not None:
                        row.append(self.state[i][j].pellet)
                        self.state[i][j].pellet = None
                    else:
                        row.append(None)
                else:
                    row.append(self.state[i][j])

            maze.append(row)
        self.state = maze 

        for ghost in self.ghosts:
            ghost.x, ghost.y = ghost.start
            self.state[ghost.y][ghost.x] = ghost

            if ghost.pellet is not None:
                self.state[ghost.last[1]][ghost.last[0]] = ghost.pellet
                ghost.pellet = None

        self.pacman.x, self.pacman.y = self.pacman.start
        self.pacman.direction = "West"
        self.pacman.next_direction = None
        self.pacman.is_respawning = True

        self.pacman.set_avatar(self.graphics)
        self.pacman.death = False

    def ghost_restore_last_square(self, ghost):
        if ghost.last is not None:
            if (ghost.y, ghost.x) != ghost.last:
                if ghost.pellet is not None:
                    self.state[ghost.last[0]][ghost.last[1]] = ghost.pellet
                    ghost.pellet = None
                else:
                    self.state[ghost.last[0]][ghost.last[1]] = None

    def pacman_location(self) -> Pacman:
        for obj in self.objects:
            if type(obj) == Pacman:
                return obj
    
    def can_change_direction(self, direction):
        y, x = self.pacman.curr_loc()

        if direction == 'South':
            return type(self.state[y + 1][x]) != Wall and (y + 1, x) not in [(13,11), (13,16)]

        elif direction == 'North':
            return type(self.state[y - 1][x]) != Wall

        else:
            return type(self.state[y][x - 1 if direction == "West" else x + 1]) != Wall

    def update_directions(self):
        self.validate_upcoming_movement()

        self.pacman.last = self.pacman.curr_loc()

        if self.can_change_direction(self.pacman.direction):
            self.pacman.run()

    def validate_upcoming_movement(self):
        if self.pacman.next_direction is not None:
            if self.can_change_direction(self.pacman.next_direction):
                self.pacman.change_direction(self.pacman.next_direction)
                self.pacman.next_direction = None
                self.pacman.set_avatar(self.graphics)