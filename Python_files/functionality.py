import pymongo
import tkinter as tk
from tkinter import ttk
from pymongo import MongoClient

#import connection string, hidden from git for security reasons
import mongodb_userinfo

cluster = MongoClient(mongodb_userinfo.connection_string())
db = cluster["592_Project_1"]

def btn_read_press(traffic,year,frame_display,label_status_display):
    if traffic == "Accidents":
        if year == "2016":
            results = results_list("Traffic_Incidents_Archive_2016")
            print_table(results,frame_display)

        if year == "2017":
            results = results_list("Traffic_Incidents_Archive_2017")
            print_table(results,frame_display)

        #TODO: 2018 file needs parsing (there is no standalone 2018 file)
        if year == "2018":
            results = results_list("Traffic_Incidents")
            print_table(results,frame_display)

    if traffic == "Traffic volume":
        if year == "2016":
            results = results_list("TrafficFlow2016_OpenData")
            print_table(results,frame_display)

        if year == "2017":
            results = results_list("2017_Traffic_Volume_Flow")
            print_table(results,frame_display)

        if year == "2018":
            results = results_list("Traffic_Volumes_for_2018")
            print_table(results,frame_display)

def btn_sort_press(traffic,year,frame_display,label_status_display):
    #TODO: add functionality to sort_button
    if traffic == "Accidents":
        if year == "2016":
            pass

        if year == "2017":
            pass

        if year == "2018":
            pass

    if traffic == "Traffic volume":
        if year == "2016":
            pass

        if year == "2017":
            pass

        if year == "2018":
            pass

def btn_analysis_press(traffic,year,frame_display,label_status_display):
    #TODO: add functionality to analysis_button
    if traffic == "Accidents":
        if year == "2016":
            pass

        if year == "2017":
            pass

        if year == "2018":
            pass

    if traffic == "Traffic volume":
        if year == "2016":
            pass

        if year == "2017":
            pass

        if year == "2018":
            pass

def btn_map_press(traffic,year,frame_display,label_status_display):
    #TODO: add functionality to map_button
    if traffic == "Accidents":
        if year == "2016":
            pass

        if year == "2017":
            pass

        if year == "2018":
            pass

    if traffic == "Traffic volume":
        if year == "2016":
            pass

        if year == "2017":
            pass

        if year == "2018":
            pass

#grid style approach to making a table
#too slow
# def print_table(result_list,frame_display):
#     list_rows = []
#     for result in result_list[0]:
#         list_rows.append([result])

#     for i in list_rows:
#         for result in result_list:
#              i.append(result[i[0]])

#     for i in range(1,len(list_rows)):
#         for j in range(len(list_rows[i])):
#             entry = tk.Entry(frame_display)
#             entry.grid(column = i, row = j)
#             entry.insert("end", list_rows[i][j])

#TODO: formatting of col width
def print_table(result_list,frame_display):

    for items in frame_display.winfo_children():
        items.destroy()

    tree = ttk.Treeview(frame_display)
    tree['show'] = 'headings'

    tree_scroll_y = ttk.Scrollbar(frame_display)
    tree_scroll_y.configure(command = tree.yview)
    tree.configure(yscrollcommand=tree_scroll_y.set)

    tree_scroll_x = ttk.Scrollbar(frame_display, orient = "horizontal")
    tree_scroll_x.configure(command = tree.xview)
    tree.configure(xscrollcommand=tree_scroll_x.set)
    
    #columns
    list_cols = []
    for result in result_list[0]:
        list_cols.append(result)
    col_names = list_cols
    tree["columns"] = col_names[1:]
    counter = 0
    for col in col_names[1:]:
        tree.heading(counter,text = col,anchor = "w")
        counter += 1

    list_rows = []
    for i in range(len(result_list)):
        list_rows.append([])
        for key,value in result_list[i].items():
            if key == "_id":
                continue
            list_rows[i].append(value)

    for i in range(len(list_rows)):
        tree.insert("",i,text = "",values = list_rows[i])

    tree_scroll_y.pack(side = "right", fill = "y")
    tree_scroll_x.pack(side = "bottom", fill = "x")
    tree.pack(side = "left",expand = 1, fill = "both")


def results_list(collection_name):
    collection = db[collection_name]
    results = list(collection.find({}))
    return results
