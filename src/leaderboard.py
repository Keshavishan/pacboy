import tkinter as tk
from tkinter import font

class Leaderboard():
    def __init__(self, parent):
        self.parent = parent
        icon = parent.graphics.get("leaderboard")
        self.button = tk.Button(parent.frame, image=icon, bg="black", command=self.screen, foreground="black", highlightthickness = 0, bd = 0)
        self.back_icon = self.parent.graphics.get('back')

    def screen(self):
        self.parent.frame.destroy()
        self.parent.base_frame()
        players = sorted(self.parent.gameplay.values(), key=lambda d: d['high_score'], reverse=True)
    
        for i, player in enumerate(players[:10]):
            message = f"{i + 1}. {player['name']} - {player['high_score']}"
            tk.Label(self.parent.frame, text=message, background="black",
                    foreground="white", font=('Arial', 24)).place(relx=.5, rely=(.35 + i/20), anchor="c")

        

        button = tk.Button(self.parent.frame, image=self.back_icon)
        button.place(relx=.5, rely=(.35 + len(players[:10]) / 10), anchor="c")

    def place_button(self):
        self.button.place(relx=.5, rely=.575, anchor="c")