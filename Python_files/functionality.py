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
        # update status
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
                # invoke results_list_2017 function which exports the collection (2017 incidents) from mongodb
                results = results_list_2017("Traffic_Incidents_Archive_2017")

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
        # update status
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

# this function handles operations when the analysis button is clicked
def btn_analysis_press(traffic,year,frame_display,label_status_display):
    try:
        #update status
        label_status_display.config(bg="#00FF00", text= "Successfully analyzed")

        # if user selects 'Accidents'
        if traffic == "Accidents":
            #prints graph of higest frequent accident area per year
            print_analysis(frame_display)

        # if user selects 'Traffic'        
        if traffic == "Traffic volume":
            #prints graph of highest volume area per year
            print_analysis2(frame_display)

    #if error occurs
    except:
         label_status_display.config(bg="red", text= "Analysis Error")

# this function handles operations when the map button is clicked
def btn_map_press(traffic,year,frame_display,label_status_display):
    try:
        #update status
        label_status_display.config(bg="#00FF00", text= "Successfully written map")

        # if user selects 'Accidents'
        if traffic == "Accidents":
            # if user selects year '2016'
            if year == "2016":
                #creates html map based on accident data
                print_map(frame_display,"Traffic_Incidents_Archive_2016_sorted_freq")
                pass
            
            # if user selects year '2017'
            if year == "2017":
                #creates html map based on accident data
                print_map(frame_display,"Traffic_Incidents_Archive_2017_sorted_freq")
                pass
            
            # if user selects year '2018'
            if year == "2018":
                #creates html map based on accident data
                print_map(frame_display,"Traffic_Incidents_Archive_2018_sorted_freq")
                pass
        
        # if user selects 'Traffic'
        if traffic == "Traffic volume":
            # if user selects year '2016'
            if year == "2016":
                #creates html map based on traffic volume data
                print_map_2(frame_display,"TrafficFlow2016_OpenData")
                pass
            
            # if user selects year '2017'
            if year == "2017":
                #creates html map based on traffic volume data
                print_map_2(frame_display,"2017_Traffic_Volume_Flow")
                pass

            # if user selects year '2018'
            if year == "2018":
                #creates html map based on traffic volume data
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
#given a list of dictionaries from DB import, create a table using Treeview
def print_table(result_list,frame_display):
    #destroy all children elements in the frame
    for items in frame_display.winfo_children():
        items.destroy()

    #initialize Treeview and scroll bar
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

    #extract column headers
    for result in result_list[0]:
        list_cols.append(result)

    #sets the number of columns needed
    tree["columns"] = list_cols[1:]

    #sets the column to the header
    counter = 0
    for col in list_cols[1:]:
        tree.heading(counter,text = col,anchor = "w")
        counter += 1

    #rows
    list_rows = []

    #converts values of the dictionary to a list format
    for i in range(len(result_list)):
        list_rows.append([])

        for key,value in result_list[i].items():
            #skips _id/row value
            if key == "_id":
                continue
            list_rows[i].append(value)

    #sets the rows from the values obtained
    for i in range(len(list_rows)):
        tree.insert("",i,text = "",values = list_rows[i])

    #packs the items into the frame
    tree_scroll_y.pack(side = "right", fill = "y")
    tree_scroll_x.pack(side = "bottom", fill = "x")
    tree.pack(side = "left",expand = 1, fill = "both")

#returns a list of the database in a given collection name
def results_list(collection_name):
    collection = db[collection_name]
    results = list(collection.find({}).sort("_id",1))

    return results

#returns a list of the database in a given collection name (only 2017 data)
def results_list_2017(collection_name):
    collection = db[collection_name]
    results = list(collection.find({}).sort("_id",1))

    results_2017 = []

    for result in results:
        if "2017" in result["START_DT"]:
            results_2017.append(result)
            
    return results_2017

#returns a list of the database in a given collection name (only 2018 data)    
def results_list_2018(collection_name):
    collection = db[collection_name]
    results = list(collection.find({}).sort("_id",1))

    results_2018 = []

    for result in results:
        if "2018" in result["START_DT"]:
            results_2018.append(result)
            
    return results_2018

#~READ END~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~ANALYSIS START~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#prints graph of higest frequent accident area per year
def print_analysis(frame_display):
    #destroy all children elements in the frame
    for items in frame_display.winfo_children():
        items.destroy()
    
    collection1 = db["Traffic_Incidents_Archive_2016_sorted_freq"]
    collection2 = db["Traffic_Incidents_Archive_2017_sorted_freq"]
    collection3 = db["Traffic_Incidents_Archive_2018_sorted_freq"]

    acc2016 = list(collection1.find({}, {"freq":1,"_id":0}))
    acc2017 = list(collection2.find({}, {"freq":1,"_id":0}))
    acc2018 = list(collection3.find({}, {"freq":1,"_id":0}))

    #~~~~~~~~~~~~2016~~~~~~~~~~~~~~~~~

    
    #create list of 2016 accidents
    list_acc2016= []
    for result in acc2016:
        list_acc2016.append(result["freq"])
    
    #find max
    accSum2016 = 0
    for i in list_acc2016:
        if i>accSum2016:
            accSum2016=i
   
    #~~~~~~~~~~~~2017~~~~~~~~~~~~~~~~~

     #create list of 2017 accidents
    list_acc2017= []
    for result in acc2017:
        list_acc2017.append(result["freq"])
    
    #find max
    accSum2017 = 0
    for i in list_acc2017:
        if i>accSum2017:
            accSum2017=i
    #~~~~~~~~~~~~2018~~~~~~~~~~~~~~~~~


     #create list of 2018 accidents
    list_acc2018= []
    for result in acc2018:
        list_acc2018.append(result["freq"])

    #find max
    accSum2018 = 0
    for i in list_acc2018:
        if i>accSum2018:
            accSum2018=i


    #create table
    table = {'Year': ['2016','2017','2018'],
             'Accidents' : [accSum2016, accSum2017, accSum2018]}
    
    df=pd.DataFrame(data=table)


    
    """
    create figure
    """
    
    #initialize figure
    fig=Figure(figsize = (5,4),dpi=100)

    #adds plot
    fig.add_subplot(1,1,1).plot(df.Year, df.Accidents, marker = 'o')
    fig.subplots_adjust(left=0.1, right=0.9, bottom=0.1)

    #adds title and labels
    fig.text(0.5, 0.04, 'Year', ha='center', size = '14')
    fig.text(0.04, 0.5, 'Maximum Accidents', va='center', rotation='vertical', size = '14')
    fig.text(0.5, 0.9, 'Maximum Accidents per Year', ha='center', size = '24')
   
    #initialize canvas widget
    canvas = FigureCanvasTkAgg(fig, frame_display)

    #pack canvas onto frame
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
   
        
    #figure tool bar, maybe not neccessary
    toolbar = NavigationToolbar2Tk(canvas, frame_display)
    toolbar.update()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

#prints graph of highest volume area per year
def print_analysis2(frame_display):
    #destroy all children elements in the frame
    for items in frame_display.winfo_children():
        items.destroy()
    
    collection1 = db["TrafficFlow2016_OpenData"]
    collection2 = db["2017_Traffic_Volume_Flow"]
    collection3 = db["Traffic_Volumes_for_2018"]

    # year2016 = list(collection1.find({}, {"year_vol":1,"_id":0}))
    volume2016 = list(collection1.find({}, {"volume":1,"_id":0}))

    # year2017 = list(collection2.find({}, {"year":1,"_id":0}))
    volume2017 = list(collection2.find({}, {"volume":1,"_id":0}))

    # year2018 = list(collection3.find({}, {"YEAR":1,"_id":0}))
    volume2018 = list(collection3.find({}, {"VOLUME":1,"_id":0}))

    #~~~~~~~~~~~~2016~~~~~~~~~~~~~~~~~

    #create list of 2016 volumes
    list_vol2016= []
    for result in volume2016:
        list_vol2016.append(result["volume"])
        
    #find max
    volSum2016 = 0
    for i in list_vol2016:
        if i>volSum2016:
            volSum2016=i
   
    #~~~~~~~~~~~~2017~~~~~~~~~~~~~~~~~

    #create list of 2017 volumes
    list_vol2017= []
    for result in volume2017:
        list_vol2017.append(result["volume"])
    
    #find max
    volSum2017 = 0
    for i in list_vol2017:
        if i>volSum2017:
            volSum2017=i
            #~~~~~~~~~~~~2018~~~~~~~~~~~~~~~~~


    #create list of 2017 volumes
    list_vol2018= []
    for result in volume2018:
        list_vol2018.append(result["VOLUME"])

    #find max
    volSum2018 = 0
    for i in list_vol2018:
        if i>volSum2018:
            volSum2018=i

    #create table to import into df
    table = {'Year': ['2016','2017','2018'],
         'Volume' : [volSum2016, volSum2017, volSum2018]}


    #import into df
    df=pd.DataFrame(data=table)
    
    """
    create figure
    """
    
    #initialize figure
    fig=Figure(figsize = (5,4),dpi=100)

    #adds plot
    fig.add_subplot(1,1,1).plot(df.Year, df.Volume, marker = 'o')
    fig.subplots_adjust(left=0.1, right=0.9, bottom=0.1)

    #adds title and labels
    fig.text(0.5, 0.04, 'Year', ha='center', size = '14')
    fig.text(0.04, 0.5, 'Maximum Traffic Volume', va='center', rotation='vertical', size = '14')
    fig.text(0.5, 0.9, 'Maximum Traffic Volume per Year', ha='center', size = '24')

    #initialize canvas widget
    canvas = FigureCanvasTkAgg(fig, frame_display)
    
    #pack canvas onto frame
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
   
    ##figure tool bar, maybe not neccessary
    toolbar = NavigationToolbar2Tk(canvas, frame_display)
    toolbar.update()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
#~ANALYSIS END~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~MAP START~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#creates html map based on accident data
def print_map(frame_display,collection_name):
    #destroy all children elements in the frame
    for items in frame_display.winfo_children():
        items.destroy()
    
    collection = db[collection_name]

    #finds the max frequency
    freq = list(collection.find({"_id":0}, {"freq":1,"_id":0}))
    max_freq = freq[0]["freq"]

    #returns a list of the rows that contain this max frequency
    Lat = list(collection.find({"freq":max_freq}, {"Latitude":1,"_id":0}).sort("_id",1))
    Long = list(collection.find({"freq":max_freq}, {"Longitude":1,"_id":0}).sort("_id",1))
    section = list(collection.find({"freq":max_freq}, {"INCIDENT INFO":1,"_id":0}).sort("_id",1))

    #creates a list of the values of the dictionaries
    list_lat = []
    for result in Lat:
        list_lat.append(result["Latitude"])
        
    list_long = []
    for result in Long:
        list_long.append(result["Longitude"])  
        
    list_section = []
    for result in section:
        list_section.append(result["INCIDENT INFO"])   
    # print(list_section)

    #determines the amount of unique locations
    section_unique = len(set(list_section))

    
    average_lat = [0]*section_unique
    average_long = [0]*section_unique
    list_freq = [max_freq]*section_unique
    #calculates the average latitude and longitude of each unique section
    for i in range(section_unique):
        average_lat[i] = sum(list_lat[i*max_freq:(i+1)*max_freq])/max_freq
        average_long[i] = sum(list_long[i*max_freq:(i+1)*max_freq])/max_freq

    # Lat = list(collection.find({}, {"Latitude":1,"_id":0}))
    # Long = list(collection.find({}, {"Longitude":1,"_id":0}))
    # Count = list(collection.find({}, {"Count":1,"_id":0}))
    
    # list_lat = []
    # for result in Lat:
    #     list_lat.append(result["Latitude"])
    
    # list_long = []
    # for result in Long:
    #     list_long.append(result["Longitude"])  
    
    # list_count = []
    # for result in Count:
    #     list_count.append(result["Count"])

    #creates dataframe from previous values    
    df=pd.DataFrame({'Latitude':average_lat,'Longitude' : average_long, 'frequency' : list_freq})
    
    #creates map object
    map_osm = folium.Map(location=[average_lat[0],average_long[0]], tiles='Stamen Toner', zoom_start=13)
    
    #places markers based on data
    for index, row in df.iterrows():
        folium.Marker(location=[row['Latitude'], row['Longitude']], popup=str(row['frequency']),icon=folium.Icon(color='red',icon='location', prefix='ion-ios')).add_to(map_osm)
   
    #saves the map in the directory
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

#creates html map based on traffic volume data
def print_map_2(frame_display,collection_name,year = 2016):
    #destroy all children elements in the frame
    for items in frame_display.winfo_children():
        items.destroy()
    
    collection = db[collection_name]
    
    #parses multiline string
    #checks if year is 2018
    if year == 2018:
        list_long, list_lat, list_volume = database_parse_multicoordinates_2018(collection)
    #otherwise use 2016/2017 parsing function
    else:
        list_long, list_lat, list_volume = database_parse_multicoordinates(collection)

    #calculates the average latitude and longitude
    average_long = [sum(list_long)/len(list_long)]
    average_lat = [sum(list_lat)/len(list_lat)]
    volume = [list_volume[0]]

    #creates dataframe from previous values     
    df=pd.DataFrame({'Latitude':average_lat,'Longitude' : average_long, 'Volume' : volume})
    
    #creates map object
    map_osm = folium.Map(location=[average_lat[0],average_long[0]], tiles='Stamen Toner', zoom_start=13)
    
    #places markers based on data
    for index, row in df.iterrows():
        folium.Marker(location=[row['Latitude'], row['Longitude']], popup=str(row['Volume']),icon=folium.Icon(color='red',icon='location', prefix='ion-ios')).add_to(map_osm)
    
    #saves the map in the directory
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
    #strips the string of everything that is not a number and splits on spaces
    s_stripped = s.replace("MULTILINESTRING","").replace("(","").replace(")","").replace(",","")
    s_split = s_stripped.split()

    list_long = []
    list_lat = []
    list_volume = int(len(s_split) /2) *[volume]

    #appends latitudes and longitudes based on long/lat/long/lat... pattern
    for i in range(len(s_split)):
        if i % 2 == 0:
            list_long.append(float(s_split[i]))
        else:
            list_lat.append(float(s_split[i]))

    return list_long,list_lat,list_volume


#given a database return a list of lats,longs and volumes
def database_parse_multicoordinates(collection):
    #parses the top x number of rows
    x = 1

    #list of multiline strings and volumes, sorted by largest volume to smallest
    results = list(collection.find({},{"the_geom": 1, "volume": 1, "_id": 0}))
    results.sort(key = itemgetter('volume'), reverse = True)

    list_long = []
    list_lat = []
    list_volume_extended = []

    #for every row, use the parse_multicoordinates function
    for result in results[:x]:
        long,lat,vol = parse_multicoordinates(result["the_geom"],result["volume"])
        list_long.extend(long)
        list_lat.extend(lat)
        list_volume_extended.extend(vol)

    #no parsing, uses the whole file
    # list_multi_line_string = list(collection.find({},{"the_geom": 1, "_id": 0}))
    # list_volume = list(collection.find({},{"volume": 1, "_id": 0}))

    # list_long = []
    # list_lat = []
    # list_volume_extended = []

    # for string,volume in zip(list_multi_line_string,list_volume):
    #     long,lat,vol = parse_multicoordinates(string["the_geom"],volume["volume"])
    #     list_long.extend(long)
    #     list_lat.extend(lat)
    #     list_volume_extended.extend(vol)

    return list_long,list_lat,list_volume_extended

#given a database return a list of lats,longs and volumes for 2018
def database_parse_multicoordinates_2018(collection):
    #parses the top x number of rows
    x = 1

    #list of multiline strings and volumes, sorted by largest volume to smallest
    results = list(collection.find({},{"multilinestring": 1, "VOLUME": 1, "_id": 0}))
    results.sort(key = itemgetter('VOLUME'), reverse = True)

    list_long = []
    list_lat = []
    list_volume_extended = []

    #for every row, use the parse_multicoordinates function
    for result in results[:x]:
        long,lat,vol = parse_multicoordinates(result["multilinestring"],result["VOLUME"])
        list_long.extend(long)
        list_lat.extend(lat)
        list_volume_extended.extend(vol)

    #no parsing, uses the whole file
    # list_multi_line_string = list(collection.find({},{"multilinestring": 1, "_id": 0}))
    # list_volume = list(collection.find({},{"VOLUME": 1, "_id": 0}))

    # list_long = []
    # list_lat = []
    # list_volume_extended = []

    # for string,volume in zip(list_multi_line_string,list_volume):
    #     long,lat,vol = parse_multicoordinates(string["multilinestring"],volume["VOLUME"])
    #     list_long.extend(long)
    #     list_lat.extend(lat)
    #     list_volume_extended.extend(vol)
        
    return list_long,list_lat,list_volume_extended
#~MAP END~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~