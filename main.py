#James Hiebert
#CS487P Winter 2020
#Project Part 1
#
#This file contains the main runnable code for Project 1 and uses functions from 
#the generate.py and dataimport.py files. Running this file will generate csv files
#containing data for the TENKTUP1, TENKTUP2, and ONEKTUP tables as specified in the
#Wisconsin Benchmark paper. If these files are already in the parent folder of this
#file they will be overwritten by newly generated data. This file will then connect
#to a database using the parameters in database.ini, check if tables TENKTUP1, TENKTUP2,
#and ONEKTUP exist in the SQL database and create them if they're not found, then import
#the data in the generated csv files into the database to populate the tables.

import generate
import dataimport

#Read database.ini to get parameters for connecting to a SQL database
with open('database.ini', 'r') as db:
    connection_string = db.read()

#Create names for SQL tables
table_names = ["TENKTUP1", "TENKTUP2", "ONEKTUP"]
#Generate filenames and number of tuples to store in the file
files = [['tenktup1.csv', 10000], ['tenktup2.csv', 10000], ['onektup.csv', 1000]]

#Create tables in db
for table in table_names:
    dataimport.createTable(table, connection_string)
#Create csv files
for file in files:
    generate.generateBenchmarkData(file[0], file[1])
#Copy data from csv files into db tables
for i in range(len(table_names)):
    dataimport.importData(files[i][0], table_names[i], connection_string)
    

