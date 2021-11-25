from tkinter import PhotoImage
import os

class Graphics():
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

    
