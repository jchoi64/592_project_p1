import tkinter as tk

class project_GUI():
    def __init__(self,window):
        window.title("592 Project")

        window.mainloop()

class proj_button(tk.Button):

    def __init__(self, *args, **kwargs):
        tk.Button.__init__(self, *args, **kwargs)
        self['width'] = 25
        self['height'] = 3
        self['bg'] = "grey"
        self['fg'] = "black"

window = tk.Tk()
gui_start = project_GUI(window)