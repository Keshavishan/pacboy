import tkinter as tk
from dot import Dot
from enemy import Enemy
from graphics import Graphics
from maze import Maze
from pacman import Pacman
from wall import Wall

class Game():
    def __init__(self, root: tk.Tk, width, height, graphics: Graphics, backFn):
        self.root = root
        self.width = 1000
        self.height = 850
        self.graphics = graphics

        self.backFn = backFn

        self.current = tk.Canvas(root, width=width, height=height, background="black")
        self.current.grid(row=0,column=0, sticky=tk.N)
        
        label = lambda: tk.Label(root, text='0', font=('Arial', 18))

        self.points, self.level, self.no_lives = label(), label(), label()

        self.points.grid(row=1, column=0, sticky=tk.W)
        self.level.grid(row=1, column=0, sticky=tk.N)
        self.no_lives.grid(row=1, column=0, sticky=tk.E)

        self.key_bindings(True)
        self.pause = False
        self.interupt = None

        self.game = Maze(graphics)
        self.game.new_level()
    
    def pause_game(self, event: tk.Event):
        self.pause = not self.pause
        self.interupt = event.keysym
    
    def draw_maze(self) -> None:
        height = self.height / self.game.m_height
        width = self.width / self.game.m_width

        for obj in self.game.objects:
            if type(obj) == Wall:
                self.current.create_rectangle(obj.x * width, obj.y * height, (obj.x * width / width + 1) * width, (obj.y * height / height + 1) * height, fill = 'dark blue', width=0)
            elif type(obj) == Pacman or type(obj) == Dot or type(obj) == Enemy:
                self.current.create_image( obj.x * width + (width / 2), obj.y * height + (height / 2), image = obj.avatar)
    
    def refresh_maze(self):
        self.current.delete(tk.ALL)
        self.draw_maze()
    
    def countdown(self):
        def number(image):
            self.refresh_maze()
            self.current.create_image(self.width / 2, self.height / 2,
                                                  image = self.graphics.get(image) )
        
        self.root.after(100, lambda: number('three'))
        self.root.after(700, lambda: number('two'))
        self.root.after(1300, lambda: number('one'))


    def check_pause(self) -> None:
        if self.pause:
            self.root.after(1, self.check_pause)
        else:
            self.update()

    def exit(self):
        self.current.destroy()
        self.backFn()
    
    
    def update(self):
        if self.pause:
            self.current.create_image(self.width / 2, self.height / 2, image = self.graphics.get("boss" if self.interupt == "b" else 'paused') )
            self.check_pause()

        else:
            self.game.update_directions()
            self.game.update_maze()
            self.root.after(125, self.update)

            if not self.game.game_over:
                self.refresh_maze()
    
    def pacmans_direction(self, event: tk.Event):
        try:
            # self.game.pacman.change_direction(event.keysym)
            if self.game.can_change_direction(event.keysym):
                print("can")
            else:
                print("cant")
            # if not self.game.can_change_direction( event.keysym ):
            #     self.game.pacman.next_direction = event.keysym
            #     self.board.pacman.direction = self.board.pacman.last_direction

            # else:
            #     self.board.pacman.direction_image( self._images )
            #     self.board.pacman.next_direction = None

        except AttributeError:
            pass

    def key_bindings(self, enabled: bool):
        if enabled:
            self.root.bind('<Escape>', self.pause_game)
            self.root.bind('<space>', self.pause_game)
            self.root.bind('b', self.pause_game)
            self.root.bind('<Left>', self.pacmans_direction)
            self.root.bind('<Right>', self.pacmans_direction)
            self.root.bind('<Up>', self.pacmans_direction)
            self.root.bind('<Down>', self.pacmans_direction)
            self.root.bind('<Down>', self.pacmans_direction)


    def run(self):
        self.countdown()
        self.root.after(2000, self.update)