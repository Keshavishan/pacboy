"""
The maze class handles the initialisation and all functionality related to the maze and the movement of objects within
it
"""

from powerPellet import PowerPellet
from pellet import Pellet
from graphics import Graphics
from helper import listmaker
from pacman import Pacman
from wall import Wall
from ghost import Ghost


class Maze:
    def __init__(self, graphics: Graphics):
        self.graphics = graphics
        self.m_width, self.m_height, self.state, self.pacman, self.ghost = None, None, None, None, None
        self.objects = set()
        self.game_over = False
        self.update_counter = 0
        self.pellets_left = 0
        self.cheats = None

    def new_level(self, saved_game={}):
        points, lives, curr_level, def_boost_time = self.stats()
        self.objects = set()
        self.ghost = None
        self.cheats = None

        mapping = [listmaker(0, 28),  # 0
                   ([0] + listmaker(2, 12) + [0]) * 2,  # 1
                   [0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 0],  # 2
                   [0, 3, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 3, 0],  # 3
                   [0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 0],  # 4
                   [0] + listmaker(2, 12) + [3] + listmaker(2, 13) + [0] + [0],  # 5
                   [0, 2, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 2, 0],  # 6
                   [0, 2, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 2, 0],  # 7
                   [0, 2, 2, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 2, 2, 0],  # 8
                   [0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, None, 0, 0, None, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0],  # 9
                   [0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, None, 0, 0, None, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0],  # 10
                   [0, 0, 0, 0, 0, 0, 2, 0, 0, None, None, None, None, None, None, None, None, None, None, 0, 0, 2, 0,
                    0, 0, 0, 0, 0],  # 11
                   [0, 0, 0, 0, 0, 0, 2, 0, 0, None, 0, None, 0, 0, 0, 0, None, 0, None, 0, 0, 2, 0, 0, 0, 0, 0, 0],
                   # 12
                   [0, 0, 0, 0, 0, 0, 2, 0, 0, None, 0, None, None, None, None, None, None, 0, None, 0, 0, 2, 0, 0, 0,
                    0, 0, 0],  # 13
                   [None, None, None, None, None, None, 2, None, None, None, 0, None, None, None, None, None, None, 0,
                    None, None, None, 2, None, None, None, None, None, None],  # 14
                   [0, 0, 0, 0, 0, 0, 2, 0, 0, None, 0, None, 4, 5, 6, 7, None, 0, None, 0, 0, 2, 0, 0, 0, 0, 0, 0],
                   # 15
                   [None, None, None, None, None, 0, 2, 0, 0, None, 0, 0, 0, 0, 0, 0, 0, 0, None, 0, 0, 2, 0, None,
                    None, None, None],  # 16
                   [None, None, None, None, None, 0, 2, 0, 0, None, None, None, None, None, None, None, None, None,
                    None, 0, 0, 2, 0, None, None, None, None, None],  # 17
                   [None, None, None, None, None, 0, 2, 0, 0, None, 0, 0, 0, 0, 0, 0, 0, 0, None, 0, 0, 2, 0, None,
                    None, None, None, None],  # 18
                   [0, 0, 0, 0, 0, 0, 2, 0, 0, None, 0, 0, 0, 0, 0, 0, 0, 0, None, 0, 0, 2, 0, 0, 0, 0, 0, 0],  # 19
                   ([0] + listmaker(2, 12) + [0]) * 2,  # 20
                   [0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 0],  # 21
                   [0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 0],  # 22
                   [0, 3, 2, 2, 0, 0, 2, 2, 2, 2, 2, 2, 2, None, 1, 2, 2, 2, 2, 2, 2, 2, 0, 0, 2, 2, 3, 0, 0],  # 23
                   [0, 0, 0, 2, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 2, 0, 0, 0],  # 24
                   [0, 0, 0, 2, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 2, 0, 0, 0],  # 25
                   [0, 2, 2, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 2, 2, 0],  # 26
                   [0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0],  # 27
                   [0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0],  # 28
                   [0] + listmaker(2, 13) + [3] + listmaker(2, 12) + [0] + [0],  # 29
                   listmaker(0, 28)  # 30
                   ]

        overrides = {
            2: {
                2: [(5, 13),(29, 14)]
            },
            3: {
                0: [(29, 7), (29, 8)]
            },
            4: {
                0: [(29, 19), (29, 20)]
            },
            5: {
                0: [(5, 13), (5, 14)]
            }
        }

        for level in overrides:
            if level < curr_level + 1:
                for override, positions in overrides[level].items():
                    for position in positions:
                        mapping[position[0]][position[1]] = override

        self.m_height, self.m_width = len(mapping), len(mapping[0])
        maze = []
        
        for i in range(len(mapping)):
            row = []
            for j in range(len(mapping[i])):
                if mapping[i][j] == Wall.id:
                    row.append(Wall(j, i, self.graphics))
                elif mapping[i][j] == Pacman.id:
                    row.append(Pacman(j, i, self.graphics, saved_game=saved_game["pacman"] if saved_game else {}))

                elif mapping[i][j] == Ghost.id:
                    row.append(Ghost(j, i, self.graphics, saved_game=saved_game["ghost"] if saved_game else {}))
                
                elif saved_game:
                    if mapping[i][j] == Pellet.id and (i, j) in saved_game["pellet_positions"]:
                        row.append(Pellet(j, i, self.graphics))

                    elif mapping[i][j] == PowerPellet.id and (i, j) in saved_game["pellet_positions"]:
                        row.append(PowerPellet(j, i, self.graphics))
                    else:
                        row.append(None)
                elif mapping[i][j] == Pellet.id:
                    row.append(Pellet(j, i, self.graphics))

                elif mapping[i][j] == PowerPellet.id:
                    row.append(PowerPellet(j, i, self.graphics))

                else:
                    row.append(None)

            maze.append(row)

        self.state = maze
        self.update_maze()

        self.pacman = self.get_pacman()
        if not saved_game:
            self.pacman.points, self.pacman.lives, self.pacman.level = points, lives, curr_level
            self.pacman.defBoostTime, self.pacman.boostTime = def_boost_time, def_boost_time

        self.ghost = self.get_ghost()

    def no_updates(self):
        return self.update_counter

    def stats(self) -> tuple:
        if self.state is not None:
            return self.pacman.points, self.pacman.lives, self.pacman.level + 1, 45 - (5 * self.pacman.level)
        else:
            return 0, 3, 1, 45

    def reset_last_square(self, game_object):
        if game_object.last is not None:
            if (game_object.y, game_object.x) != game_object.last:
                previous_y, previous_x = game_object.last

                if type(self.state[previous_y][previous_x]) is None and not self.pacman.is_respawning:
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

        pellets = {p for p in self.objects if type(p) in [Pellet, PowerPellet]}

        self.pellets_left = len(pellets)

        self.update_game_state()

    def get_pacman(self) -> Pacman:
        for obj in self.objects:
            if type(obj) == Pacman:
                return obj

    def get_ghost(self) -> Ghost:
        for obj in self.objects:
            if type(obj) == Ghost:
                return obj

    def update_game_state(self):
        y, x = self.pacman.curr_loc()

        # Pacman location
        if (y == 14 and x == 0) or (y == 14 and x == 27):
            self.pacman.teleport()
            self.state[self.pacman.y][self.pacman.y] = self.pacman
        else:
            self.pacman.collision(self.state[y][x])
        
        # Pacman boost
        if self.pacman.invulnerable:
            if self.pacman.boostTime == self.pacman.defBoostTime:
                if self.ghost:
                    self.ghost.invulnerable = True
                    self.ghost.set_avatar(self.ghost.name, self.graphics)
                if not self.pacman.invincible:
                    self.pacman.boostTime -= 1

            elif self.pacman.boostTime == 0:
                if self.ghost:
                    self.ghost.invulnerable = False
                    self.ghost.set_avatar(self.ghost.name, self.graphics)
                self.pacman.boostTime = self.pacman.defBoostTime
                self.pacman.invulnerable = not self.pacman.invulnerable

            else:
                if not self.pacman.invincible:
                    self.pacman.boostTime -= 1

        # Enemy
        if self.ghost:
            if self.update_counter % 2 or self.pellets_left < 100 + (20 * self.pacman.level) or (
                    self.pacman.level > 3 and self.pacman.lives < 2) or self.ghost.send_to_initial_position:
                self.ghost.move(self, self.pacman)
                self.reset_last_square(self.ghost)

                if self.ghost.send_to_initial_position:
                    self.ghost.send_to_initial_position = False
                    self.ghost_to_initial_position()

                elif (self.ghost.y, self.ghost.x) == (y, x):
                    if not self.ghost.invulnerable:
                        self.lose_life_update_game()
                    else:
                        self.pacman.collision(self.ghost)
                        self.ghost_to_initial_position()

                else:
                    self.ghost_restore_last_square(self.ghost)
                    if type(self.state[self.ghost.y][self.ghost.x]) in [Pellet, PowerPellet]:
                        self.ghost.pellet = self.state[self.ghost.y][self.ghost.x]
                    if type(self.state[self.ghost.y][self.ghost.x]) != Wall:
                        self.state[self.ghost.y][self.ghost.x] = self.ghost

        if self.ghost_incoming(x):
            if not self.ghost.invulnerable:
                self.lose_life_update_game()

        elif not self.game_over:
            self.reset_last_square(self.pacman)
            self.state[y][x] = self.pacman

        else:
            self.state[y][x] = None

    def ghost_incoming(self, x) -> bool:
        if x != self.m_width - 1 and x != 0:
            if self.pacman.last:
                dy, dx = self.pacman.last
                return type(self.state[dy][dx]) == Ghost
        

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
                elif type(self.state[i][j]) in [Ghost]:
                    if self.state[i][j].pellet is not None:
                        row.append(self.state[i][j].pellet)
                        self.state[i][j].pellet = None
                    else:
                        row.append(None)
                else:
                    row.append(self.state[i][j])

            maze.append(row)
        self.state = maze

        self.ghost_to_initial_position()

        self.pacman.x, self.pacman.y = self.pacman.start
        self.pacman.direction = "West"
        self.pacman.next_direction = None
        self.pacman.is_respawning = True

        self.pacman.set_avatar(self.graphics)
        self.pacman.death = False
        self.state[self.pacman.y][self.pacman.x] = self.pacman

    def ghost_to_initial_position(self):
        if self.ghost:
            self.ghost.x, self.ghost.y = self.ghost.start
            self.state[self.ghost.y][self.ghost.x] = self.ghost

            if self.ghost.pellet is not None:
                self.state[self.ghost.last[0]][self.ghost.last[1]] = self.ghost.pellet
                self.ghost.pellet = None

    def ghost_restore_last_square(self, ghost):
        if ghost.last is not None:
            if (ghost.y, ghost.x) != ghost.last:
                if ghost.pellet is not None:
                    self.state[ghost.last[0]][ghost.last[1]] = ghost.pellet
                    ghost.pellet = None
                else:
                    self.state[ghost.last[0]][ghost.last[1]] = None

    def can_change_direction(self, direction):
        y, x = self.pacman.curr_loc()

        if direction == 'South':
            return type(self.state[y + 1][x]) != Wall and (y + 1, x) not in [(13, 11), (13, 16)]

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
