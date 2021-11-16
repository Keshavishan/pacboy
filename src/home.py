import tkinter as tk
from graphics import Graphics
from game import Game

class Home():
    def __init__(self, root: tk.Tk):
        self.root = root
        self.width = 1000
        self.height = 850
        self.graphics = Graphics()

        self.create_frame()
        
    def create_frame(self):
        self.frame = tk.Frame(self.root, width=self.width, height=self.height, background="black")
        self.frame.pack(expand=True, fill=tk.BOTH)
        
        pacman_logo = self.graphics.get("Pacman")
        tk.Label(self.frame, image = pacman_logo, background="black", borderwidth = 0, bd=0).place(relx=.5, rely=.2, anchor="c")
        
        self.play()
        self.leaderboard()
        self.exit()

    def play(self):
        icon = self.graphics.get("play")
        button = tk.Button(self.frame, image=icon, command= self.start_game, bg="black", foreground="black", highlightthickness = 0, bd = 0)
        button.place(relx=.5, rely=.5, anchor="c")
    
    def start_game(self):
        self.frame.destroy()
        game = Game(self.root, self.width, self.height, self.graphics, self.create_frame)
        game.run()

    def leaderboard(self):
        icon = self.graphics.get("leaderboard")
        button = tk.Button(self.frame, image=icon, command= self.start_game, background="black", highlightthickness = 0, bd = 0)
        button.place(relx=.5, rely=.575, anchor="c")

    def exit(self):
        icon = self.graphics.get("exit")
        button = tk.Button(self.frame, image=icon, command= self.root.destroy, bg="black", foreground="black", highlightthickness = 0, bd = 0)
        button.place(relx=.5, rely=.65, anchor="c")