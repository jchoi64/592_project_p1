#import required libraries
import pymongo
from pymongo import MongoClient
import pandas as pd
import os

#import connection string, hidden from git for security reasons
import mongodb_userinfo


def insert_collection_freq(file_name):
    #collection name removes the .csv portion of the file name
    file_name_trimmed = file_name[:-4]
    file_name_trimmed = file_name_trimmed + "_sorted_freq"
    collection = db[file_name_trimmed]

    #organizes the csv into a dictionary
    file = pd.read_csv(file_name)
    file['freq'] = file.groupby('INCIDENT INFO')['INCIDENT INFO'].transform('count')
    file = file.sort_values(['freq', 'INCIDENT INFO'], ascending=[False, False])
    result = file.to_dict('records')

    #sets the _id of each list element
    #i.e the _id is the row number
    counter = 0
    for i in result:
        i["_id"] = counter
        counter += 1

    #inserts the dictionary into mongodb
    try:
        collection.insert_many(result)
    except:
        print("Problem in inserting: ",file_name)

def extract_2018_accidents(file_name):
    data = pd.read_csv(file_name)
    data = data[data["id"].str.startswith('2018')]
    return data

def insert_collection_freq_2018(file_name):
    #collection name removes the .csv portion of the file name
    collection = db["Traffic_Incidents_Archive_2018_sorted_freq"]

    #organizes the csv into a dictionary
    file = extract_2018_accidents(file_name)
    file['freq'] = file.groupby('INCIDENT INFO')['INCIDENT INFO'].transform('count')
    file = file.sort_values(['freq', 'INCIDENT INFO'], ascending=[False, False])
    result = file.to_dict('records')

    #sets the _id of each list element
    #i.e the _id is the row number
    counter = 0
    for i in result:
        i["_id"] = counter
        counter += 1

    #inserts the dictionary into mongodb
    try:
        collection.insert_many(result)
    except:
        print("Problem in inserting: ",file_name)

cluster = MongoClient(mongodb_userinfo.connection_string())
db = cluster["592_Project_1"]

files = ["Traffic_Incidents_Archive_2016.csv","Traffic_Incidents_Archive_2017.csv"]

#make sure you are in the csv directory file
for file in files:
    insert_collection_freq(file)

insert_collection_freq_2018("Traffic_Incidents.csv")