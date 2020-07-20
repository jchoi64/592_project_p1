import pymongo
from pymongo import MongoClient

import pymongo
import tkinter as tk
from tkinter import ttk
import numpy as np

import pandas as pd
import csv

import folium
from folium.plugins import MarkerCluster
import webbrowser
import os

from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib import style

from operator import itemgetter

#import connection string, hidden from git for security reasons
import mongodb_userinfo

cluster = MongoClient(mongodb_userinfo.connection_string())
db = cluster["592_Project_1"]

# this function handles operations when the read button is clicked
def btn_read_press(traffic,year,frame_display,label_status_display):
    try:
        # update Status
        label_status_display.config(bg="#00FF00", text= "Successfully read from DB")
        
        # if user selects 'Accidents'
        if traffic == "Accidents":
            # if user selects year '2016'
            if year == "2016":
                # invoke results_list function which exports the collection (2016 incidents) from mongodb
                # assign the list to 'results'
                results = results_list("Traffic_Incidents_Archive_2016")
                # print the table in GUI
                print_table(results,frame_display)

            # if user selects year '2017'
            if year == "2017":
                # invoke results_list function which exports the collection (2017 incidents) from mongodb
                results = results_list("Traffic_Incidents_Archive_2017")
                # print the table in GUI
                print_table(results,frame_display)

            # if user selects year '2018'
            if year == "2018":
                # unlike year 2016 and 2017, there is no separate file for just the year of 2018
                # results_list_2018 function extracts 2018 incidents from the 'Traffic_Incidents' collection
                # invoke results_list_2018 function which exports collection from mongodb and extracts 2018 data
                results = results_list_2018("Traffic_Incidents")
                # print the table in GUI
                print_table(results,frame_display)

        # if user selects 'Volume'
        if traffic == "Traffic volume":
            # if user selects year '2016'
            if year == "2016":
                # invoke results_list function which exports the collection (2016 traffic volume) from mongodb
                results = results_list("TrafficFlow2016_OpenData")
                # print the table in GUI
                print_table(results,frame_display)
            
            # if user selects year '2017'
            if year == "2017":
                # invoke results_list function which exports the collection (2017 traffic volume) from mongodb
                results = results_list("2017_Traffic_Volume_Flow")
                # print the table in GUI
                print_table(results,frame_display)
            
            # if user selects year '2018'
            if year == "2018":
                # invoke results_list function which exports the collection (2018 traffic volume) from mongodb
                results = results_list("Traffic_Volumes_for_2018")
                # print the table in GUI
                print_table(results,frame_display)
    
    #if error occurs
    except:
        # display error message in the status window, in this case it would be 'Error Reading from DB'
        label_status_display.config(bg="red", text= "Error Reading from DB")


# this function handles operations when the sort button is clicked
def btn_sort_press(traffic,year,frame_display,label_status_display):
    try:
        # Update States
        label_status_display.config(bg="#00FF00", text= "Successfully sorted")
        
        # if user selects 'Accidents'
        if traffic == "Accidents":
            # if user selects year '2016'
            if year == "2016":
                # invoke results_list function which exports the collection (sorted 2016 incidents) from mongodb
                # assign the list to 'results'
                results = results_list("Traffic_Incidents_Archive_2016_sorted_freq")
                # print the table in GUI
                print_table(results,frame_display)
            
            # if user selects year '2017'
            if year == "2017":
                # invoke results_list function which exports the collection (sorted 2017 incidents) from mongodb
                # assign the list to 'results'
                results = results_list("Traffic_Incidents_Archive_2017_sorted_freq")
                # print the table in GUI
                print_table(results,frame_display)

            # if user selects year '2018'
            if year == "2018":
                # invoke results_list function which exports the collection (sorted 2018 incidents) from mongodb
                results = results_list("Traffic_Incidents_Archive_2018_sorted_freq")
                # print the table in GUI
                print_table(results,frame_display)

        # if user selects 'Volume'
        if traffic == "Traffic volume":
            # if user selects year '2016'
            if year == "2016":
                # invoke results_list function which exports the collection (2016 traffic volume) from mongodb
                # assign the list to 'results'
                results = results_list("TrafficFlow2016_OpenData")
                # sort the 'results' list
                # 'itemgetter' is imported from the 'operator' module
                # select all the keys associated with volume, then sort the list in descending order of volume
                results.sort(key = itemgetter('volume'), reverse = True)
                # print the table in GUI
                print_table(results,frame_display)

            # if user selects year '2017'
            if year == "2017":
                # invoke results_list function which exports the collection (2017 traffic volume) from mongodb
                # assign the list to 'results'
                results = results_list("2017_Traffic_Volume_Flow")
                # sort the 'results' list
                # 'itemgetter' is imported from the 'operator' module
                # select all the keys associated with volume, then sort the list in descending order of volume
                results.sort(key = itemgetter('volume'), reverse = True)
                # print the table in GUI
                print_table(results,frame_display)
            
            # if user selects year '2018'
            if year == "2018":
                # invoke results_list function which exports the collection (2018 traffic volume) from mongodb
                # assign the list to 'results'
                results = results_list("Traffic_Volumes_for_2018")
                # sort the 'results' list
                # 'itemgetter' is imported from the 'operator' module
                # select all the keys associated with volume, then sort the list in descending order of volume
                results.sort(key = itemgetter('VOLUME'), reverse = True)
                # print the table in GUI
                print_table(results,frame_display)
    
    #if error occurs
    except:
        # display error message in the status window, in this case it would be 'sort error'
        label_status_display.config(bg="red", text= "Sort Error")


def btn_analysis_press(traffic,year,frame_display,label_status_display):
    try:
        #update Status
        label_status_display.config(bg="#00FF00", text= "Successfully analyzed")
        if traffic == "Accidents":
            print_analysis(frame_display,"Traffic_Incidents")
                
        if traffic == "Traffic volume":
            print_analysis2(frame_display,"Traffic_Incidents")

    #if error occurs
    except:
         label_status_display.config(bg="red", text= "Analysis Error")


def btn_map_press(traffic,year,frame_display,label_status_display):
    try:
        #update Status
        label_status_display.config(bg="#00FF00", text= "Successfully written map")
        if traffic == "Accidents":
            if year == "2016":
                print_map(frame_display,"Traffic_Incidents_Archive_2016")
                pass

            if year == "2017":
                print_map(frame_display,"Traffic_Incidents_Archive_2017")
                pass
            
            #TODO: fix 2018 html
            if year == "2018":
                print_map(frame_display,"Traffic_Incidents_Archive_2018")
                pass
        
        #TODO: currently creates huge html files that basically cant be loaded, needs less markers somehow (some sort of grouping required or instead of markers, heat map?)
        if traffic == "Traffic volume":
            if year == "2016":
                print_map_2(frame_display,"TrafficFlow2016_OpenData")
                pass

            if year == "2017":
                print_map_2(frame_display,"2017_Traffic_Volume_Flow")
                pass

            if year == "2018":
                print_map_2(frame_display,"Traffic_Volumes_for_2018", 2018)
                pass
    #if error occurs
    except:
         label_status_display.config(bg="red", text= "Map Error")

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

#~READ START~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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

    
def results_list_2018(collection_name):
    collection = db[collection_name]
    results = list(collection.find({}))

    results_2018 = []

    for result in results:
        if "2018" in result["START_DT"]:
            results_2018.append(result)
            
    return results_2018

#~READ END~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~ANALYSIS START~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def print_analysis(frame_display,collection_name):
    
    for items in frame_display.winfo_children():
        items.destroy()
    
    #create colelction
    collection = db[collection_name]
    #create lists of needed data
    year = list(collection.find({}, {"START_DT":1,"_id":0}))
    id_ = list(collection.find({}, {"id":1,"_id":0}))
    Count= list(collection.find({}, {"Count":1,"_id":0}))


    list_year = []
    #format lists
    for result in year:
        list_year.append(result["START_DT"])
    
    #output only year in a list (explude month, day and time)
    list_year2= [x[6:-12] for x in list_year]    
   
    #print(list_year2) <--- used as a check
 
    list_id = []
    #format lists
    for result in id_:
        list_id.append(result["id"])  

    list_count = []
    #format lists
    for result in Count:
        list_count.append(result["Count"])
      
    #create dataframe by combining lists
    df=pd.DataFrame({'Year':list_year2,'Count':list_count})

    #sort dataframe
    df2=df['Year'].value_counts().to_frame('y').rename_axis('Year').reset_index()
    df2=df2.sort_values("Year",axis=0, ascending = True)

    #print(df2) <-- used as a check
    
    """
    create figure
    """
    
    fig=Figure(figsize = (5,4),dpi=100)

    a=fig.add_subplot(1,1,1).plot(df2.Year, df2.y)
    fig.subplots_adjust(left=0.1, right=0.9, bottom=0.1) 
   

    canvas = FigureCanvasTkAgg(fig, frame_display)
    #fig.set_xlabel('x')
    #fig.set_ylabel('y')

    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
   
        
    ##figure tool bar, maybe not neccessary
    toolbar = NavigationToolbar2Tk(canvas, frame_display)
    toolbar.update()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


def print_analysis2(frame_display,collection_name):
    
    for items in frame_display.winfo_children():
        items.destroy()
    
    collection1 = db["TrafficFlow2016_OpenData"]
    collection2 = db["2017_Traffic_Volume_Flow"]
    collection3 = db["Traffic_Volumes_for_2018"]

    year2016 = list(collection1.find({}, {"year_vol":1,"_id":0}))
    volume2016 = list(collection1.find({}, {"volume":1,"_id":0}))

    year2017 = list(collection2.find({}, {"year":1,"_id":0}))
    volume2017 = list(collection2.find({}, {"volume":1,"_id":0}))

    year2018 = list(collection3.find({}, {"YEAR":1,"_id":0}))
    volume2018 = list(collection3.find({}, {"VOLUME":1,"_id":0}))

    #~~~~~~~~~~~~2016~~~~~~~~~~~~~~~~~

    list_vol2016= []
    for result in volume2016:
        list_vol2016.append(result["volume"])
    
    volSum2016 = 0
    for i in list_vol2016:
        volSum2016 += i
   
    #~~~~~~~~~~~~2017~~~~~~~~~~~~~~~~~

    list_vol2017= []
    for result in volume2017:
        list_vol2017.append(result["volume"])
    
    volSum2017 = 0
    for i in list_vol2017:
        volSum2017 += i

    #~~~~~~~~~~~~2018~~~~~~~~~~~~~~~~~

    list_vol2018= []
    for result in volume2018:
        list_vol2018.append(result["VOLUME"])

    volSum2018 = 0
    for i in list_vol2018:
        volSum2018 += i

    table = {'Year': ['2016','2017','2018'],
             'Volume' : [volSum2016, volSum2017, volSum2018]}



    df=pd.DataFrame(data=table)
    
    """
    create figure
    """
    
    fig=Figure(figsize = (5,4),dpi=100)

    a=fig.add_subplot(1,1,1).plot(df.Year, df.Volume)
    fig.subplots_adjust(left=0.1, right=0.9, bottom=0.1) 
   

    canvas = FigureCanvasTkAgg(fig, frame_display)
    #fig.set_xlabel('x')
    #fig.set_ylabel('y')

    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
   
        
    ##figure tool bar, maybe not neccessary
    toolbar = NavigationToolbar2Tk(canvas, frame_display)
    toolbar.update()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
#~ANALYSIS END~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~MAP START~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def print_map(frame_display,collection_name):
    
    for items in frame_display.winfo_children():
        items.destroy()
    
    collection = db[collection_name]
    Lat = list(collection.find({}, {"Latitude":1,"_id":0}))
    Long = list(collection.find({}, {"Longitude":1,"_id":0}))
    Count = list(collection.find({}, {"Count":1,"_id":0}))
    
    list_lat = []
    for result in Lat:
        list_lat.append(result["Latitude"])
    
    list_long = []
    for result in Long:
        list_long.append(result["Longitude"])  
    
    list_count = []
    for result in Count:
        list_count.append(result["Count"])
        
    df=pd.DataFrame({'Latitude':list_lat,'Longitude' : list_long, 'Count' : list_count})
    
    
    #can I make it start on looking at locaiton of most accidents?
    map_osm = folium.Map(location=[51.0673798693422,-114.028551292521], tiles='Stamen Toner', zoom_start=13)
    
    for index, row in df.iterrows():
        folium.Marker(location=[row['Latitude'], row['Longitude']], popup=str(row['Count']),icon=folium.Icon(color='red',icon='location', prefix='ion-ios')).add_to(map_osm)
   
    map_osm
    map_osm.save('C:/Users/Jun/Documents/uofc work/ENSF 592/Project/HTML_files/map.html')

   # webbrowser.open(url,new=ne2)
    
    #webbrowser.open('file://' + os.path.realpath('map_osm'))
    
    """
    try:
        from uirllib import pathname2url
    except:
        from urllib.request import pathname2url
        
    url = format(pathname2url(os.path.abspath('map_osm')))
    webbrowser.open(url)
    """

    pass


def print_map_2(frame_display,collection_name,year = 2016):
    
    for items in frame_display.winfo_children():
        items.destroy()
    
    collection = db[collection_name]
    
    #checks if year is 2018
    if year == 2018:
        list_long, list_lat, list_volume = database_parse_multicoordinates_2018(collection)
    #otherwise use 2016/2017 parsing function
    else:
        list_long, list_lat, list_volume = database_parse_multicoordinates(collection)

        
    df=pd.DataFrame({'Latitude':list_lat,'Longitude' : list_long, 'Volume' : list_volume})
    
    
    #can I make it start on looking at locaiton of most accidents?
    map_osm = folium.Map(location=[51.0673798693422,-114.028551292521], tiles='Stamen Toner', zoom_start=13)
    
    for index, row in df.iterrows():
        folium.Marker(location=[row['Latitude'], row['Longitude']], popup=str(row['Volume']),icon=folium.Icon(color='red',icon='location', prefix='ion-ios')).add_to(map_osm)
   
    map_osm
    map_osm.save('C:/Users/Jun/Documents/uofc work/ENSF 592/Project/HTML_files/map.html')

   # webbrowser.open(url,new=ne2)
    
    #webbrowser.open('file://' + os.path.realpath('map_osm'))
    
    """
    try:
        from uirllib import pathname2url
    except:
        from urllib.request import pathname2url
        
    url = format(pathname2url(os.path.abspath('map_osm')))
    webbrowser.open(url)
    """

    pass


#given a MULTILINESTRING s and volume, return list of longs and list of lats with their count/volume
def parse_multicoordinates(s,volume):
    s_stripped = s.replace("MULTILINESTRING","").replace("(","").replace(")","").replace(",","")
    s_split = s_stripped.split()

    list_long = []
    list_lat = []
    list_volume = int(len(s_split) /2) *[volume]

    for i in range(len(s_split)):
        if i % 2 == 0:
            list_long.append(s_split[i])
        else:
            list_lat.append(s_split[i])

    return list_long,list_lat,list_volume


#given a database return a list of longs,lats and volumes
def database_parse_multicoordinates(collection):
    list_multi_line_string = list(collection.find({},{"the_geom": 1, "_id": 0}))
    list_volume = list(collection.find({},{"volume": 1, "_id": 0}))

    list_long = []
    list_lat = []
    list_volume_extended = []

    for string,volume in zip(list_multi_line_string,list_volume):
        long,lat,vol = parse_multicoordinates(string["the_geom"],volume["volume"])
        list_long.extend(long)
        list_lat.extend(lat)
        list_volume_extended.extend(vol)

    return list_long,list_lat,list_volume_extended


#given a database return a list of longs,lats and volumes for 2018
def database_parse_multicoordinates_2018(collection):
    list_multi_line_string = list(collection.find({},{"multilinestring": 1, "_id": 0}))
    list_volume = list(collection.find({},{"VOLUME": 1, "_id": 0}))

    list_long = []
    list_lat = []
    list_volume_extended = []

    for string,volume in zip(list_multi_line_string,list_volume):
        long,lat,vol = parse_multicoordinates(string["multilinestring"],volume["VOLUME"])
        list_long.extend(long)
        list_lat.extend(lat)
        list_volume_extended.extend(vol)
        
    return list_long,list_lat,list_volume_extended
#~MAP END~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~