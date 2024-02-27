from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base
from flask import Flask, jsonify, render_template
from sqlalchemy.orm import sessionmaker
import json


import pandas as pd

app = Flask(__name__)

engine = create_engine("postgresql://project_3_333t_user:3LuhMTGZ77yugy4ExOkIqqROOtWMs4rE@dpg-cnbuglv79t8c73ep52q0-a.ohio-postgres.render.com/project_3_333t", echo=False)

Base = automap_base()
Base.prepare(engine, reflect=True)

School_Location = Base.classes.School_Location_2


# Main Route

@app.route('/')
def main():

    message = "Work in progres <br> Possible routes: <br> /tables <br> /map <br> /school_locations"
    return message

#Table Names Route PROVVISORY

@app.route('/tables')
def visualize_tables():
    engine = create_engine("postgresql://project_3_333t_user:3LuhMTGZ77yugy4ExOkIqqROOtWMs4rE@dpg-cnbuglv79t8c73ep52q0-a.ohio-postgres.render.com/project_3_333t", echo=False)
    inspector = inspect(engine)
    table_names = inspector.get_table_names()

    tables = {}
    for table_name in table_names:
        columns = inspector.get_columns(table_name)
        tables[table_name] = [column["name"] for column in columns]

    return jsonify(tables)

#School Locations Route

@app.route('/school_locations')
def get_school_locations():
    Session = sessionmaker(bind=engine)
    session = Session()

    results = session.query(School_Location).all()
    print(results)

    school_data = []

    for result in results:
        school_data.append({
            "school_name": result.School_Number,
            "latitude": result.Latitude,
            "longitude": result.Longitude
        })

    session.close()

    return jsonify(school_data)
    
# Map Route

@app.route("/map")
def map():
    return render_template('index.html')

# Debugging Function 

if __name__ == "__main__":
    app.run(debug = True)