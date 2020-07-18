import tkinter as tk
from tkinter import ttk
from functionality import *

class project_GUI(tk.Tk):

    def __init__(self,*args, **kwargs):
        tk.Tk.__init__(self,*args, **kwargs)

        #window properties
        self.title("592 Project")
        self.geometry("1500x750")

        #frames
        frame_buttons = tk.Frame(
            master = self,
            height = 750,
            width = 300,
            bg = "grey",
        )

        frame_display = tk.Frame(
            master = self,
            height = 750,
            width = 1200,
            bg = "green",
        )

        #items to be added to frame_buttons
        list_btn = []

        #combo boxes
        combo_traffic = ttk.Combobox(
            master = frame_buttons,
            font = "36",
            values = [
                "Accidents",
                "Traffic volume"
            ]
        )
        combo_traffic.current(0)
        list_btn.append(combo_traffic)

        combo_years = ttk.Combobox(
            master = frame_buttons,
            font = "36",
            values = [
                "2016",
                "2017",
                "2018"
            ]
        )
        combo_years.current(0)
        list_btn.append(combo_years)

        #buttons
        # list_btn_strings = ["Read","Sort","Analysis","Map"]

        # for i in list_btn_strings:
        #     list_btn.append(proj_button(
        #         text = i,
        #         master = frame_buttons,
        #         command = lambda i = i: button_click(i),
        #     ))

        btn_read = proj_button(
            text = "Read",
            master = frame_buttons,
            command = lambda: btn_read_press(combo_traffic.get(),combo_years.get()),
        )
        list_btn.append(btn_read)

        btn_sort = proj_button(
            text = "Sort",
            master = frame_buttons,
            command = lambda: btn_sort_press(combo_traffic.get(),combo_years.get()),
        )
        list_btn.append(btn_sort)

        btn_analysis = proj_button(
            text = "Analysis",
            master = frame_buttons,
            command = lambda: btn_analysis_press(combo_traffic.get(),combo_years.get()),
        )
        list_btn.append(btn_analysis)

        btn_map = proj_button(
            text = "Map",
            master = frame_buttons,
            command = lambda: btn_map_press(combo_traffic.get(),combo_years.get()),
        )
        list_btn.append(btn_map)

        #status display
        label_status = tk.LabelFrame(
            master = frame_buttons,
            text = "Status",
            font = 20,
            bg = "grey",
        )

        #TODO: update status display depending on success/failure
        label_status_display = tk.Label(
            master = label_status,
            width = 20,
            height = 5,
            font = 36,
            text = "To be updated",
            bg = "light green",
        )
        label_status_display.pack(expand = True,fill = "both")
        list_btn.append(label_status)

        #adds list_btn to frame_button grid style
        for i in range(len(list_btn)):
            frame_buttons.rowconfigure(i, weight = 1, minsize = 50)
            list_btn[i].grid(row = i, padx = 5, pady = 5)

        #items to be added to frame_display
        #TODO: update display after pressing button
        display = tk.Label(
            text = "Output will go here",
            master = frame_display,
            height = 750,
            width = 1200,
            # bg = "green",
            )
        display.pack(expand = True,fill = "both")

        #packs frames left to right and fits the size of the window
        frame_buttons.pack(expand = True,fill = "y",side = "left")
        frame_display.pack(expand = True,fill = "both",side = "right")

    def run_GUI(self):
        self.mainloop()

class proj_button(tk.Button):

    def __init__(self, *args, **kwargs):
        tk.Button.__init__(self, *args, **kwargs)
        self['width'] = 15
        self['height'] = 2
        self['font'] = "36"
        self['bg'] = "#d3d3d3"
        self['fg'] = "black"

#TODO: add other classes for other elements in the GUI

gui = project_GUI()
gui.run_GUI()