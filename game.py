import sys
import tkinter as tk
from tkinter.constants import CENTER
from powerPellet import PowerPellet
from pellet import Pellet
from ghost import Ghost
from maze import Maze
from pacman import Pacman
from wall import Wall

class Game():
    def __init__(self, parent):
        self.root = parent.root
        self.width = parent.width
        self.height = parent.height
        self.graphics = parent.graphics
        self.parent = parent
        self.current = tk.Canvas(parent.root, width=parent.width, height=parent.height, background="black")
        self.current.grid(row=0, column=0, sticky=tk.N)

        def label(): return tk.Label(parent.root, text='0', font=('Arial', 18))

        self.points, self.level, self.no_lives = label(), label(), label()

        self.points.grid(row=1, column=0, sticky=tk.W)
        self.level.grid(row=1, column=0, sticky=tk.N)
        self.no_lives.grid(row=1, column=0, sticky=tk.E)

        self.options = {option['key']: option for option in self.parent.user["options"]}

        self.key_bindings(True)
        self.pause = False
        self.interupt = None

        self.game = Maze(parent.graphics)
        self.game.new_level(self.parent.user["saved_game"])

        self.cheat_bindings(True)

        self.used_cheats = []

    def pause_game(self, event):
        self.pause = not self.pause
        self.interupt = event.keysym

    def draw_maze(self) -> None:
        height = self.height / self.game.m_height
        width = self.width / self.game.m_width

        for obj in self.game.objects:
            if type(obj) == Wall:
                self.current.create_rectangle(obj.x * width, obj.y * height, (obj.x * width / width + 1)
                                              * width, (obj.y * height / height + 1) * height, fill='dark blue', width=0)
            elif type(obj) in [Pacman, Pellet, PowerPellet, Ghost]:
                self.current.create_image(
                    obj.x * width + (width / 2), obj.y * height + (height / 2), image=obj.avatar)

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
                                      image=self.graphics.get(image))

        self.root.after(100, lambda: number('three'))
        self.root.after(700, lambda: number('two'))
        self.root.after(1300, lambda: number('one'))

    def check_pause(self, button: tk.Button) -> None:
        if self.pause:
            self.root.after(1, lambda: self.check_pause(button))
        else:
            button.destroy()
            self.update()

    def exit(self, gameOver = True):
        self.current.destroy()
        self.points.destroy()
        self.level.destroy()
        self.no_lives.destroy()

        if gameOver:
            self.parent.save_score(self.game.pacman.points)
            self.parent.user["saved_game"] = []
        self.parent.menu()


    def show_image_screen(self, image):
        self.current.create_image(
            self.width / 2, self.height / 2, image=self.graphics.get(image))

    def to_next_level(self):
        self.game.new_level()
        self.key_bindings(True)

    def handle_next_level(self):
        self.current.delete(tk.ALL)
        self.used_cheats = []
        self.show_image_screen("loading")
        self.parent.save_progress(self.game.pacman.lives, self.game.pacman.level, self.game.pacman.points)
        self.root.after(3500, self.to_next_level)

    def back(self):
        button = tk.Button(self.current, image=self.graphics.get(
            'back'), command=lambda: self.exit(self.game.game_over))
        
        button.place(x=((self.width - button.winfo_reqwidth())/2),
                     y=self.height/2 + 150)

        return button

    def update(self):
        if self.pause:
            self.show_image_screen(
                'boss' if self.return_key_name(self.interupt) == "Boss Key" else 'paused')
            button = self.back()
            self.check_pause(button)
            pass
        else:
            self.game.update_directions()
            self.game.update_maze()

            if self.game.pellets_left == 0:
                self.game.pacman.direction = None
                self.key_bindings(False)
                self.root.after(750, self.handle_next_level)
                self.current.after(5000, lambda: self.run(False))

            elif self.game.game_over:
                self.key_bindings(False)
                self.game.pacman.avatar = None
                self.show_image_screen("game_over")
                self.back()

            elif self.game.pacman.is_respawning:
                self.game.pacman.is_respawning = False
                self.draw_maze()
                self.root.after(550, lambda: self.run(True))

            else:
                self.current.after(125, self.update)

            if not self.game.game_over:
                self.refresh_maze()
    
    def return_key_name(self, key):
        if self.options.get(key, False):
            return self.options[key]['name']
        elif self.options.get(f'<{key}>', False):
            return self.options[f'<{key}>']['name']

    def change_direction(self, event):
        mapping = {
            "Up": "North",
            "Down": "South",
            "Left": "West",
            "Right": "East",
        }

        direction = mapping[self.return_key_name(event.keysym)]

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

    def key_bindings(self, enabled):
        keys = [
            (self.options[option]['key'], self.pause_game if self.options[option]['type'] == "pause" else self.change_direction) for option in self.options]
        self.bind_keys(keys, enabled)

    def add_lives(self, event: tk.Event):
        if "add_lives" not in self.used_cheats:
            self.game.pacman.lives += 3
            self.used_cheats.append("add_lives")

    def send_ghost_to_hut(self, event: tk.Event):
        if "send_ghost_to_hut" not in self.used_cheats:
            self.game.ghost.send_to_initial_position = True
            self.used_cheats.append("send_ghost_to_hut")    
    
    def cheat_bindings(self, enabled):
        keys = [("<Control-Shift-L>", self.add_lives), ("<Control-Shift-Alt_L>", self.send_ghost_to_hut)]
        self.bind_keys(keys, enabled)

    def bind_keys(self, keys, enabled: bool):
        if enabled:
            for key in keys:
                self.root.bind(key[0], key[1])
            for key in keys:
                self.root.unbind(key)

    def run(self, respawning):
        if respawning:
            self.refresh_maze()
        self.countdown()
        self.root.after(2100, self.update)
