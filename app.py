from flask import Flask
from flask import jsonify
from flask import render_template
from flask import request
from flask import url_for
from flask import redirect

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Import the database connection.
import db_conn


app = Flask(__name__)

#################################################
# CONVERT SQLALCHEMY TO PYTHON DICTIONARY
#################################################  

def create_grants_dict(r):
    return {
    "1. Awarded Faculty": r[0],   
    "2. Sponsor" :  r[1],
    "3. Agency Type" : r[2],
    "4. Species" : r[3],
    "5. Program Areas" : r[4],
    "6. Link" : r[5],
    "7. Application Dates" : r[6]
    } 

#################################################
# Flask Routes
#################################################  

#*************** WEBPAGES***********************#
# Renders index page
@app.route("/")
def index():
    return render_template('index.html')


# ************************************
# RETURNS WARNINGS SEVERITY CATEGORY
# ************************************

@app.route("/categories")
def return_award_categories():
    """Return a list of cuisine categories"""
    table_categories = db_conn.session.query(db_conn.awards.species.distinct()).order_by(db_conn.awards.species).all()

    # converts a list of list into a single list (flattens list)
    category_list = [item for sublist in list(table_categories) for item in sublist]

    # return a list of column names (sample names)
    return jsonify(category_list)


# ************************************
# RETURNS GRANT AWARD TABLE
# ************************************
@app.route("/filtered_awards/<species>", methods=['GET'])
def return_filtered_awards(species):

    # Step 1: set up columns needed for this run
    
    sel = [db_conn.awards.awardedfaculty, db_conn.awards.sponsors, db_conn.awards.agency_types, db_conn.awards.species, db_conn.awards.program_areas, db_conn.awards.links, db_conn.awards.application_dates]

    # Step 2: Run and store filtered query in results variable 
    results = db_conn.session.query(*sel).filter(db_conn.awards.species == species).all()

    # Step 3: Build a list of dictionary that contains all the earthquakes
    filtered = []
    for r in results:
        transformed_dict = create_grants_dict(r)
        filtered.append(transformed_dict)


    return jsonify(filtered)


    # ************************************
# RETURNS GRANT AWARD TABLE
# ************************************
@app.route("/all_awards", methods=['GET'])
def return_all_awards():

    # Step 1: set up columns needed for this run
    
    sel = [db_conn.awards.awardedfaculty, db_conn.awards.sponsors, db_conn.awards.agency_types, db_conn.awards.species, db_conn.awards.program_areas, db_conn.awards.links, db_conn.awards.application_dates]

    # Step 2: Run and store filtered query in results variable 
    results = db_conn.session.query(*sel).all()

    # Step 3: Build a list of dictionary that contains all the earthquakes
    all_awards = []
    for r in results:
        transformed_dict = create_grants_dict(r)
        all_awards.append(transformed_dict)


    return jsonify(all_awards)






if __name__ == "__main__":
    app.run()
