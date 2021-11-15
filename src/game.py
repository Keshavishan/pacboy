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

        self.game = Maze(graphics)
        self.game.new_level()
    
    def pause_game(self, event):
        self.pause = not self.pause
    
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
            self.current.create_image(self.width / 2, self.height / 2, image = self.graphics.get('paused') )
            self.check_pause()

        else:
            self.game.update_directions()
            # self.game.update_board()
            self.root.after(125, self.update)

            if not self.game.game_over:
                self.refresh_maze()
    
    def key_bindings(self, enabled: bool):
        if enabled:
            self.root.bind('<Escape>', self.pause_game)
            self.root.bind('<space>', self.pause_game)

    def run(self):
        self.countdown()
        self.root.after(2000, self.update)