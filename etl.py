# Import dependencies
import requests
import json
import pandas as pd

## Connecting to the database
import mysql.connector as mysql
from decimal import Decimal
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from pandas.io import sql

def extract_transform_load(): 

    db = mysql.connect(
        host = "127.0.0.1",
        user = "root",
        passwd = "root"
    )
    cursor = db.cursor()
    cursor.execute("DROP DATABASE IF EXISTS westernu_db")
    cursor.execute("CREATE DATABASE IF NOT EXISTS westernu_db")
    cursor.execute("USE westernu_db")
    engine = create_engine('mysql+pymysql://root:root@127.0.0.1/westernu_db', echo=False)


    #################################################
    # CREATE TABLES
    #################################################

    # Create grants table
    cursor.execute("CREATE TABLE IF NOT EXISTS awards (id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, awardedfaculty VARCHAR(255), sponsors VARCHAR(255), agency_types VARCHAR(255), species VARCHAR(255), program_areas TEXT, links TEXT, application_dates VARCHAR(255)) ENGINE=InnoDB")


    #################################################
    # LOAD AWARDED GRANTS TABLE
    #################################################
    # Load csv data
    awarded_grants_df = pd.read_csv('resources/CVM_Awards.csv')

    # Load table
    awarded_grants_df.to_sql('awards', con=engine, if_exists='append', index = False, index_label = "id")


extract_transform_load()


