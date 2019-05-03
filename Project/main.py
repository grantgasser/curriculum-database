## Group Project
## Grant Gasser, Zee Dugar, Jackson O'Donnell

## Main file for the database program with GUI

import gui as g
import create_tables as create
import mysql.connector as conn

#global constants
USER = 'root'
HOST = 'localhost'
SCHEMA_NAME = 'curriculum_db'

def connect_server(password):
    mydb = conn.connect(
        host = HOST,
        user = USER,
        passwd = password
    )

    return mydb

def connect_db(password, db):
    mydb = conn.connect(
        host = HOST,
        user = USER,
        passwd = password,
        database = db
    )

    return mydb


def main():
    schema_exists = False
    quit = False

    #read password
    infile = open('password.txt', 'r')
    password = infile.read()

    #remove newline
    password = password[:-1]

    infile.close()

    print('\nConnecting to database...\n')

    #establish connection to db
    mydb = connect_server(password)
    #print(mydb)

    #set cursor
    mycursor = mydb.cursor()

    #Make or remake curriculum database, then use it
    mycursor.execute('DROP DATABASE IF EXISTS ' + SCHEMA_NAME)
    mycursor.execute('CREATE DATABASE IF NOT EXISTS ' + SCHEMA_NAME)

    #Connect to schema (db) within server
    mydb = connect_db(password, SCHEMA_NAME)

    print('Connected to database:', SCHEMA_NAME, '\n')

    #reset mycursor
    mycursor = mydb.cursor()

    #reset mycursor
    mycursor = mydb.cursor()

    #create tables
    print("Creating tables...\n")

    create.create_tables(mycursor)

    mycursor.execute("SHOW TABLES")

    print("Here are the tables in the " + SCHEMA_NAME, "schema/database:")
    for table in mycursor:
        print(table[0])

    print('\nOpening GUI...\n')
    gui = g.MyGUI(mycursor)

    gui.show_tables()




main()
