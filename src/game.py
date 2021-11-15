import tkinter as tk
from graphics import Graphics
from maze import Maze

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

    
    def pause_game(self, event):
        self.pause = not self.pause

    def key_bindings(self, enabled: bool):
        if enabled:
            self.root.bind('<Escape>', self.pause_game)
            self.root.bind('<space>', self.pause_game)

    def check_pause(self) -> None:
        if self.pause:
            self.root.after(1, self.check_pause)
        else:
            self.update()

    def exit(self):
        self.current.destroy()
        self.backFn()

    def paused_screen(self):
        self.current.create_image(self.width / 2, self.height / 2, image = self.graphics.get('paused') )
        button1 = tk.Button(self.current, text = "Quit", image=self.graphics.get("back"), command=self.exit, anchor = tk.W)
        button1.configure(width = 10, activebackground = "#33B5E5", relief = tk.FLAT)
        self.current.create_window(10, 10, anchor=tk.NW, window=button1)

    def update(self) -> None:
        if self.pause:
            self.paused_screen()
            self.check_pause()

    def run(self):
        self.root.after(500, self.update)