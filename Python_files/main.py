import tkinter as tk
from tkinter import ttk

class project_GUI():
    def __init__(self,window):
        window.title("592 Project")
        window.geometry("500x500")

        #frames
        frame_buttons = tk.Frame(
            master = window,
            # width = 30,
            # height = 500,
            bg = "yellow",
            borderwidth = 15
        )
        # frame_buttons.grid(row = 1, column = 1, padx = 5, pady = 5)
        frame_display = tk.Frame(
            master = window
        )
        # frame_display.grid(row = 1, column = 2, padx = 5, pady = 5)

        #items to be added to frame_buttons
        list_btn = []

        #combo box
        combo_traffic = ttk.Combobox(
            master = frame_buttons,
            values = [
                "Accidents",
                "Traffic volume"
            ]
        )
        list_btn.append(combo_traffic)

        combo_years = ttk.Combobox(
            master = frame_buttons,
            values = [
                "2016",
                "2017",
                "2018"
            ]
        )
        list_btn.append(combo_years)


        #buttons
        list_btn_strings = ["Read","Sort","Analysis","Map"]

        for i in list_btn_strings:
            list_btn.append(proj_button(
                text = i,
                master = frame_buttons
            ))

        #status display    

        for i in list_btn:
            i.pack()

        #items to be added to frame_display
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