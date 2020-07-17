import pymongo
from pymongo import MongoClient
import pandas as pd
import mongodb_userinfo
import os

def insert_collection(file_name):
    file_name_trimmed = file_name[:-4]
    collection = db[file_name_trimmed]


    file = pd.read_csv(file_name)
    result = file.to_dict(orient = 'records')

    counter = 0
    for i in result:
        i["_id"] = counter
        counter += 1
    try:
        collection.insert_many(result)
    except:
        print("Problem in inserting: ",file_name)
    

cluster = MongoClient(mongodb_userinfo.connection_string())
db = cluster["592_Project_1"]

#make sure you are in csv directory file
files = os.listdir()

for file in files:
    insert_collection(file)

