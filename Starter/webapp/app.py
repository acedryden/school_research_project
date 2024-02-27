from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base
from flask import Flask, jsonify, render_template

import pandas as pd

app = Flask(__name__)

test_file = "school_location_data.csv"


@app.route('/')
def main():
    message = "Work in progres <br> Possible routes: <br> /api/v1.0/school_locations <br> /plot/bikes/for/now"
    return message

@app.route('/plot/bikes/for/now')
def PlotBikes():
    return render_template("index.html")

@app.route("/api/v1.0/school_locations")
def School_data():

    #engine = create_engine("sqlite:///dow.sqlite",echo=False)
    #Base = automap_base()
    #Base.prepere(autoload_with = engine)
    #Dow = Base.classes.dow

    #session = Session(engine)
    #result = session.query(dow).all()
    #session.close()

    School_locations_df = pd.read_csv(test_file)
    data = School_locations_df.to_dict(orient = "records") 

    return jsonify({"data" : data})



if __name__ == "__main__":
    app.run(debug = True)