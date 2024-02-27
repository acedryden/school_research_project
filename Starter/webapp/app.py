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

    engine = create_engine("postgresql://project_3_333t_user:3LuhMTGZ77yugy4ExOkIqqROOtWMs4rE@dpg-cnbuglv79t8c73ep52q0-a.ohio-postgres.render.com/project_3_333t", echo=False)
    Base = automap_base()
    Base.prepare(autoload_with=engine)
    School_Location = Base.classes.School_Location
    session=Session(engine)
    data= session.query( School_Location.Street).all()
    for row in data:
        print(row) 

    session.close()

    return jsonify({"data" : "data"})



if __name__ == "__main__":
    app.run(debug = True)