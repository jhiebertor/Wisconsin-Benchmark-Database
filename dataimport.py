#James Hiebert
#CS487P Winter 2020
#Project part 1
#
#This file contains two functions which create tables in a specified SQL 
#database to hold the Wisconsin Benchmark data, and which upload CSV files 
#to populate these tables, respectively. 
#Both functions make use of the psycopg2 module, which contains functions
#for connecting to a postgreSQL database and running queries and commands.

import psycopg2

#Connect to pSQL database and create tables
def createTable(tablename, connection_string):
    conn = psycopg2.connect(connection_string)
    cur = conn.cursor()
    #Check if the given tables already exist before trying to create them
    command_string = "SELECT EXISTS(SELECT * FROM information_schema.tables WHERE table_name='" + tablename + "')"
    cur.execute(command_string)
    #Fetch results of the above select statement
    exists = cur.fetchone()
    if(not exists): #If tables are not in db
        command_string = "CREATE TABLE " + tablename + """ (
                    unique1 integer NOT NULL,
                    unique2 integer NOT NULL PRIMARY KEY,
                    two integer NOT NULL,
                    four integer NOT NULL,
                    ten integer NOT NULL,
                    twenty integer NOT NULL,
                    hundred integer NOT NULL,
                    thousand integer NOT NULL,
                    twothous integer NOT NULL,
                    fivethous integer NOT NULL,
                    tenthous integer NOT NULL,
                    odd100 integer NOT NULL,
                    even100 integer NOT NULL,
                    stringu1 char(52) NOT NULL,
                    stringu2 char(52) NOT NULL,
                    string4 char(52) NOT NULL
                    )"""
        
        cur.execute(command_string)
        #Commit changes and close connection
        conn.commit()
        cur.close()
        conn.close()
        
#Given a csv file and a table in a specified pSQL db, upload data from 
#the file to populate the table
def importData(filename, tablename, connection_string):
    #Connect to pSQL database
    conn = psycopg2.connect(connection_string)
    cur = conn.cursor()
    #check if table exists in the database
    command_string = "SELECT EXISTS(SELECT * FROM information_schema.tables WHERE table_name='" + tablename + "')"
    cur.execute(command_string)
    exists = cur.fetchone()
    if(exists):
        with open(filename) as file:
            cur.copy_from(file, tablename, sep=',')
            conn.commit()
    cur.close()
    conn.close()
