# Wisconsin-Benchmark-Database
CS487P Project 1. The project uses postgreSQL hosted on PSU's pSQL database with the help of the psycopg2 python module. Proof of data uploaded to TENKTUP1 table: [https://imgur.com/a/yVTgkO2](https://imgur.com/a/yVTgkO2)

## Dependencies:
The psycopg2 python module is required to run these files, install it with "pip install psycopg2" from the command line.

## Main.py
The main script you'll run, this will generate new csv files with the Wisconsin Benchmark data, connect to a postgreSQL database, create tables to store benchmark data and copy data from the generated csv files into the pSQL tables.

## generate.py
Contains a function for generating csv files with Wisconsin Benchmark data

## dataimport.py
Contains functions for creating pSQL tables in a provided pSQL database and populating these tables with data from provided csv files.

## database.ini
Holds the connection string needed to connect to a pSQL database, this file must be edited to include database connection info prior to running main.py.

## Provided .csv files
These csv files contain pre-generated data from the function in generate.py according to the specifications in the Wisconsin Benchmark paper. These will be overwritten with newly generated data each time main.py is run.

## Using this code:
Run using "python main.py" from the command line. 
Login details for connecting to a SQL database are stored in database.ini. Before running these scripts, edit the database.ini file to include the database name, name of the user, password for the user, and the host address that the database is located at (add an optional "port=####" argument if the database does not accept connections from the default port). Be sure to delete the brackets so that the first line of database.ini looks like: dbname=hiebert ...
