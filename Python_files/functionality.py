import pymongo
from pymongo import MongoClient

#import connection string, hidden from git for security reasons
import mongodb_userinfo

cluster = MongoClient(mongodb_userinfo.connection_string())
db = cluster["592_Project_1"]

def btn_read_press(traffic,year,display,label_status_display):
    #TODO: add functionality to read_button
    if traffic == "Accidents":
        if year == "2016":
            collection = db["Traffic_Incidents_Archive_2016"]
            results = collection.find({})

            display.config(text = results)
            label_status_display.config(text = "Accidents 2016")
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

def btn_sort_press(traffic,year,display,label_status_display):
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

def btn_analysis_press(traffic,year,display,label_status_display):
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

def btn_map_press(traffic,year,display,label_status_display):
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
