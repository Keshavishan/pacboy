import tkinter as tk
from tkinter.constants import CENTER
from boost import Boost
from dot import Dot
from ghosts import *
from graphics import Graphics
from maze import Maze
from pacman import Pacman
from wall import Wall

class Game():
    def __init__(self, root: tk.Tk, width, height, graphics: Graphics, create_frame):
        self.root = root
        self.width = 1000
        self.height = 850
        self.graphics = graphics
        self.create_frame = create_frame

        self.username = ""

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
            elif type(obj) in [Pacman, Dot, Boost, Inky, Pinky, Blinky, Clyde]:
                self.current.create_image( obj.x * width + (width / 2), obj.y * height + (height / 2), image = obj.avatar)
    
    def refresh_maze(self):
        self.current.delete(tk.ALL)
        self.draw_maze()
        self.no_lives['text'] = f'Lives: {self.game.pacman.lives}'
        self.level['text'] = f'Level: {self.game.pacman.level}'
        self.points['text'] = f'Points: {self.game.pacman.points}'

    
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
        self.points.destroy()
        self.level.destroy()
        self.no_lives.destroy()

        self.create_frame()

    def show_image_screen(self, image):
        self.current.create_image( self.width / 2, self.height / 2, image = self.graphics.get(image) )

    def to_next_level(self):
        self.game.new_level()
        self.key_bindings(True)
    
    def handle_next_level(self):
        self.current.delete(tk.ALL)
        self.show_image_screen("loading")
        self.root.after(3500, self.to_next_level)
           
    def update(self):
        if self.pause:
            self.show_image_screen('boss' if self.interupt == "b" else 'paused')
            # button = tk.Button(self.current, image=self.graphics.get('back'), command=self.exit)
            # button.place(x=((self.width - button.winfo_reqwidth())/2), y=self.height/2 + 150)
            self.check_pause()

        else:
            self.game.update_directions()
            self.game.update_maze()
            
            total_pickups = { p for p in self.game.objects if type(p) in [Dot, Boost] }
            
            if len(total_pickups) == 0:
                self.game.pacman.direction = None
                self.key_bindings(False)
                self.root.after(750, self.handle_next_level)
                self.current.after(5000, self.run)

            else:
                self.current.after(125, self.update)

            if not self.game.game_over:
                self.refresh_maze()
    
    def change_direction(self, event: tk.Event):
        mapping = {
            "Up": "North",
            "Down": "South",
            "Left": "West",
            "Right": "East",
            "w": "North",
            "s": "South",
            "a": "West",
            "d": "East",
        }
        direction = mapping[event.keysym]
        try:
            self.game.pacman.change_direction(direction)
            if self.game.can_change_direction(direction):
               self.game.pacman.set_avatar(self.graphics)
               self.game.pacman.next_direction = None
            else:
                self.game.pacman.next_direction = direction
                self.game.pacman.direction = self.game.pacman.last_direction

        except AttributeError:
            pass

    def key_bindings(self, enabled: bool):
        if enabled:
            self.root.bind('<Escape>', self.pause_game)
            self.root.bind('<space>', self.pause_game)
            self.root.bind('b', self.pause_game)
            self.root.bind('<Left>', self.change_direction)
            self.root.bind('<Right>', self.change_direction)
            self.root.bind('<Up>', self.change_direction)
            self.root.bind('<Down>', self.change_direction)
            self.root.bind('a', self.change_direction)
            self.root.bind('d', self.change_direction)
            self.root.bind('w', self.change_direction)
            self.root.bind('s', self.change_direction)
        else:
            self.root.unbind('<Escape>')
            self.root.unbind('<space>')
            self.root.unbind('b')
            self.root.unbind('<Left>')
            self.root.unbind('<Right>')
            self.root.unbind('<Up>')
            self.root.unbind('<Down>')
            self.root.unbind('a')
            self.root.unbind('d')
            self.root.unbind('w')
            self.root.unbind('s')
        
    
    # def set_user(self, input):
    #     print(input)

    # def user(self):
    #     self.current.delete(tk.ALL)
    #     input = tk.Entry(self.current, textvariable="Player name", background="white", fg="black")
    #     input.place(x=((self.width - input.winfo_reqwidth())/2), y=self.height/2)
    #     button = tk.Button(self.current, textvariable="Submit", fg="blue")
    #     print(input.winfo_height())
    #     button.place(x=((self.width - button.winfo_reqwidth())/2), y=self.height/2 + input.winfo_height() + 10)
    
    def run(self):
        # self.root.after(100, self.user)
        self.countdown()
        self.root.after(2000, self.update)
        