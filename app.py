from sqlalchemy import create_engine, inspect 
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base
from flask import Flask, jsonify, render_template
from sqlalchemy.orm import sessionmaker
import json


import pandas as pd

app = Flask(__name__)


# Main Route

@app.route('/')
def main():

    return render_template('home.html')


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

@app.route('/api/v1.0/School_Data')
def get_school_data():

    engine = create_engine("postgresql://project_3_333t_user:3LuhMTGZ77yugy4ExOkIqqROOtWMs4rE@dpg-cnbuglv79t8c73ep52q0-a.ohio-postgres.render.com/project_3_333t", echo=False)

    Base = automap_base()
    Base.prepare(engine, reflect=True)

    School_Data = Base.classes.School_info

    
    Session = sessionmaker(bind=engine)
    session = Session()

    School_results = session.query(School_Data).all()

    Schools = []

    

    return jsonify(Schools)

    
# Map Route

@app.route("/map")
def map():
    return render_template('index.html')

# Debugging Function 

if __name__ == "__main__":
    app.run(debug = True)