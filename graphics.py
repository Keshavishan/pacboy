"""
The graphics class imports all assets and saves them in the format required by tkinter so that time isn't wasted
reading from files multiple times.
"""

import os
from tkinter import PhotoImage


class Graphics:
    def __init__(self):
        loc = os.getcwd()

        if loc.split('/')[-1] == "src":
            img_dir = f'../assets'
        else:
            img_dir = f'{loc}/assets'

        self.graphics = {}

        for file in os.listdir(img_dir):
            self.graphics[file[:-4]] = PhotoImage(file= f'{img_dir}/{file}')

    def get(self, path) -> PhotoImage:
        return self.graphics[path]

