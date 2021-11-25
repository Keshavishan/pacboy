import tkinter as tk
from home import Home


class Window():
    def __init__(self, root: tk.Tk):
        self.root = root

        self.root.resizable(width=False, height=False)
        self.root.title('Pacman')

        Home(self.root)

    def run(self) -> None:
        self.root.mainloop()


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('1600x900')
    pacman = Window(root)
    pacman.run()
