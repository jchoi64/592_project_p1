import tkinter as tk

class project_GUI():
    def __init__(self,window):
        window.title("592 Project")
        window.geometry("500x500")

        frame_buttons = tk.Frame(
            master = window,
            width = 30,
            height = 500,
            bg = "yellow"
        )
        frame_display = tk.Frame()

        list_btn = []
        list_btn_strings = ["Read","Sort","Analysis","Map"]

        for i in list_btn_strings:
            list_btn.append(proj_button(
                text = i,
                master = frame_buttons
            ))

        for i in list_btn:
            i.pack()

        display = tk.Label(
            text = "Output will go here",
            master = frame_display
            )
        display.pack()

        frame_display.pack(side = tk.RIGHT)
        frame_buttons.pack(side = tk.LEFT)
        
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