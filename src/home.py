import tkinter as tk
import os
import pickle
from graphics import Graphics
from game import Game

class Home():
    def __init__(self, root: tk.Tk):
        self.root = root
        self.width = 1000
        self.height = 850
        self.input = None
        self.graphics = Graphics()
        self.frame = None
        self.user = {}
        self.new_user = True
        self.loc = os.getcwd()
        self.game = ""
        try:
            dbfile = open(f'{self.loc}/gameplay.pickle', 'rb')
            self.gameplay = pickle.load(dbfile)
            dbfile.close()
        except:
             self.gameplay = {}

        self.create_frame()

    def create_frame(self):
        self.frame = tk.Frame(self.root, width=self.width, height=self.height, background="black")
        self.frame.pack(expand=True, fill=tk.BOTH)
        pacman_logo = self.graphics.get("pacman")
        tk.Label(self.frame, image=pacman_logo, background="black", borderwidth = 0, bd=0).place(relx=.5, rely=.2, anchor="c")

        if self.user:
            self.welcome()
            self.play()
            self.leaderboard()
            self.exit()

        else:
            self.login()
        
    def authenticate(self):
        player = self.input.get()
        if player.lower() in self.gameplay:
            self.new_user = False
            self.user = self.gameplay[player.lower()]
        
        self.user = {"name": player}

        self.gameplay[player.lower()] = self.user

        dbfile = open(f'{self.loc}/gameplay.pickle', 'ab')

        pickle.dump(self.gameplay, dbfile)                     
        dbfile.close()

        self.frame.destroy()
        self.create_frame()


    def login(self):
        tk.Label(self.frame, text="Username", background="black", foreground="white").place(relx=.5, rely=.55, anchor="c")
        self.input = tk.Entry(self.frame, textvariable="Player name", background="white", fg="black")
        self.input.place(relx=.5, rely=.6, anchor="c")
        button = tk.Button(self.frame, textvariable="Submit", background="black", foreground="white", command=self.authenticate)
        button.place(relx=.5, rely=.7, anchor="c")


    def welcome(self):
        message = f"Welcome{' back ' if not self.new_user else ' '}{self.user.get('name', '')}"
        tk.Label(self.frame, text=message, background="black", foreground="white").place(relx=.5, rely=.4, anchor="c")

    def play(self):
        icon = self.graphics.get("play")
        button = tk.Button(self.frame, image=icon, command= self.start_game, bg="black", foreground="black", highlightthickness = 0, bd = 0)
        button.place(relx=.5, rely=.5, anchor="c")
    
    def start_game(self):
        self.frame.destroy()
        self.game = Game(self.root, self.user, self.width, self.height, self.graphics, self.create_frame)
        self.game.run(False)

    def leaderboard(self):
        icon = self.graphics.get("leaderboard")
        button = tk.Button(self.frame, image=icon, command= self.start_game, background="black", highlightthickness = 0, bd = 0)
        button.place(relx=.5, rely=.575, anchor="c")

    def exit(self):
        icon = self.graphics.get("exit")
        button = tk.Button(self.frame, image=icon, command= self.root.destroy, bg="black", foreground="black", highlightthickness = 0, bd = 0)
        button.place(relx=.5, rely=.65, anchor="c")