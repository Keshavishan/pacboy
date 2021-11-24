import tkinter as tk

class Options():
    def __init__(self, parent):
        self.parent = parent
        icon = parent.graphics.get("options")
        self.button = tk.Button(parent.frame, image=icon, bg="black", command=self.screen, foreground="black", highlightthickness = 0, bd = 0)
        self.inputs = {}
        self.options = {}

    def key(self, pos, name, key):
        label = tk.Label(self.parent.frame, text=name, background="black", foreground="white")
        input = tk.Entry(self.parent.frame, background="white", fg="black")
        input.insert(0, key)

        label.place(relx=.5, rely=(.25 + pos), anchor="c")
        input.place(relx=.5, rely=(.3 + pos), anchor="c")

        return (name, input)

    def save_preferences(self):
        new_options = []
        for option in self.options:
            option['key'] = self.inputs[option['name']].get()
            new_options.append(option)
        self.parent.user["options"] = new_options
        self.parent.return_to_menu()

    def screen(self):
        self.parent.frame.destroy()
        self.parent.base_frame()
        self.options = self.parent.user["options"]
        inputs = {}

        for i, j in enumerate(self.options):
            input = self.key(i/10, j["name"], j["key"])
            inputs[input[0]] = input[1]
        
        self.inputs = inputs
        
        button = tk.Button(self.parent.frame, text="Save", foreground="black", command=self.save_preferences)
        button.place(relx=.5, rely=(.2 + (len(self.options) + 0.5)/10), anchor="c")

    def place_button(self):
        self.button.place(relx=.5, rely=.65, anchor="c")