#import required libraries
import pymongo
from pymongo import MongoClient
import pandas as pd
import os

#import connection string, hidden from git for security reasons
import mongodb_userinfo

# extracts accidents by year 
def extract_accidents_by_year(file_name, year):
    data = pd.read_csv(file_name)
    data = data[data["id"].str.startswith(str(year))]
    return data

def insert_collection_freq_by_year(file_name, year):
    #collection name removes the .csv portion of the file name
    collection = db["Traffic_Incidents_Archive_" + str(year) + "_sorted_freq"]

    #organizes the csv into a dictionary
    file = extract_accidents_by_year(file_name, year)
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

for year in range(2016, 2019):
    insert_collection_freq_by_year("Traffic_Incidents.csv", year)
