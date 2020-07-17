#import required libraries
import pymongo
from pymongo import MongoClient
import pandas as pd
import os

#import connection string, hidden from git for security reasons
import mongodb_userinfo

#creates a collection in mongodb of the csv
def insert_collection(file_name):
    #collection name removes the .csv portion of the file name
    file_name_trimmed = file_name[:-4]
    collection = db[file_name_trimmed]

    #organizes the csv into a dictionary
    file = pd.read_csv(file_name)
    result = file.to_dict(orient = 'records')

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

#make sure you are in the csv directory file
files = os.listdir()

for file in files:
    insert_collection(file)

