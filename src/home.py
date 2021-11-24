import tkinter as tk
import os
import pickle
from graphics import Graphics
from game import Game
from leaderboard import Leaderboard
from options import Options


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
        self.screen = 0

        try:
            dbfile = open(f'{self.loc}/gameplay.pickle', 'rb')
            self.gameplay = pickle.load(dbfile)
            dbfile.close()
        except:
            self.gameplay = {}

        self.menu()

        # newlist = 

    def save_score(self, score):
        prev_score = self.user["high_score"]
        self.user["high_score"] = score if score > prev_score else prev_score

    def save_progress(self, lives, level, points):
        self.user["saved_game"] = [lives, level, points]

    def base_frame(self):
        frame = tk.Frame(self.root, width=self.width,
                              height=self.height, background="black")
        frame.pack(expand=True, fill=tk.BOTH)

        pacman_logo = self.graphics.get("pacman")
        label = tk.Label(frame, image=pacman_logo,
                         background="black", borderwidth=0, bd=0)
        label.place(relx=.5, rely=.15, anchor="c")

        self.frame = frame

    def return_to_menu(self):
        self.frame.destroy()
        self.menu()

    def menu(self):
        self.base_frame()
        menu_items = [Leaderboard(self), Options(self)]

        if self.screen == 0:
            self.login()

        elif self.screen == 1:
            self.welcome()
            self.play()
           
            for menu_item in menu_items:
                menu_item.place_button()
            self.exit()

    def authenticate(self):
        player = self.input.get()
        if player:
            if player.lower() in self.gameplay:
                self.new_user = False
                self.user = self.gameplay[player.lower()]
            else:
                self.user = {
                    "name": player,
                    "high_score": 0,
                    "saved_game": [],
                    "options": [
                        {
                            "name": "Pause",
                            "key": "<space>",
                            "type": "pause"
                        },
                        {
                            "name": "Boss Key",
                            "key": "b",
                            "type": "pause"
                        },
                        {
                            "name": "Up",
                            "key": "<Up>",
                            "type": "direction"
                        },
                        {
                            "name": "Right",
                            "key": "<Right>",
                            "type": "direction"
                        },
                        {
                            "name": "Down",
                            "key": "<Down>",
                            "type": "direction"
                        },
                        {
                            "name": "Left",
                            "key": "<Left>",
                            "type": "direction"
                        }
                    ]
                }

                self.gameplay[player.lower()] = self.user

                dbfile = open(f'{self.loc}/gameplay.pickle', 'wb')

                pickle.dump(self.gameplay, dbfile)
                dbfile.close()

            self.frame.destroy()
            self.screen = 1
            self.menu()

    def login(self):
        tk.Label(self.frame, text="Username", background="black",
                 foreground="white").place(relx=.5, rely=.45, anchor="c")
        self.input = tk.Entry(
            self.frame, textvariable="Player name", background="white", fg="black")
        self.input.place(relx=.5, rely=.5, anchor="c")
        button = tk.Button(self.frame, text="Submit",
                           foreground="black", command=self.authenticate)
        button.place(relx=.5, rely=.55, anchor="c")

    def welcome(self):
        message = f"Welcome{' back ' if not self.new_user else ' '}{self.user.get('name', '')}"
        tk.Label(self.frame, text=message, background="black",
                 foreground="white").place(relx=.5, rely=.35, anchor="c")

        if self.user["high_score"]:
            tk.Label(self.frame, text=f"Your high score is: {self.user['high_score']}", background="black", foreground="white").place(
                relx=.5, rely=.4, anchor="c")

    def play(self):
        icon = self.graphics.get("play")
        button = tk.Button(self.frame, image=icon, command=self.start_game,
                           bg="black", foreground="black", highlightthickness=0, bd=0)
        button.place(relx=.5, rely=.5, anchor="c")

    def start_game(self):
        self.frame.destroy()
        self.game = Game(self)
        self.game.run(False)

    def exit_sequence(self):
        dbfile = open(f'{self.loc}/gameplay.pickle', 'wb')
        pickle.dump(self.gameplay, dbfile)
        dbfile.close()
        self.root.destroy()

    def exit(self):
        icon = self.graphics.get("exit")
        button = tk.Button(self.frame, image=icon, command=self.exit_sequence,
                           bg="black", foreground="black", highlightthickness=0, bd=0)
        button.place(relx=.5, rely=.725, anchor="c")
