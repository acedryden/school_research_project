import pandas as pd
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, text, inspect, func
from flask import Flask, jsonify, render_template

engine = create_engine("postgresql://project_3_333t_user:3LuhMTGZ77yugy4ExOkIqqROOtWMs4rE@dpg-cnbuglv79t8c73ep52q0-a.ohio-postgres.render.com/project_3_333t", echo=False)
Base = automap_base()
Base.prepare(autoload_with=engine)
elementary = Base.classes.Enrollment
school_info = Base.classes.School_info
app = Flask(__name__)


@app.route("/")
def dow_data():
    return render_template('Jumbo.html')


@app.route("/site")
def website():
    return render_template('index.html')


@app.route("/idk")
def school_map():
    session = Session(engine)

    school_lat = session.query(school_info.Latitude).all()
    school_long = session.query(school_info.Longitude).all()

    school_lat_list = [float(row[0]) for row in school_lat]
    school_long_list = [float(row[0]) for row in school_long]

    data = {"Latitude" : school_lat_list, "Longitude" : school_long_list}

    session.close()
    return jsonify(data)

@app.route("/v0")
def welcome():
    session = Session(engine)

    schoolnums = session.query(elementary.School_Number).all()
    grade8 = session.query(elementary.Grade_8_Enrolment).all()

    school_num = [row[0] for row in schoolnums]
    grade_8 = [row[0] for row in grade8]

    data = {"School_Number" : school_num, "Grade_8_Enrolment" : grade_8}
    
    session.close()
    return jsonify(data)

@app.route("/close")
def wewb():
    return render_template('test.html')

if __name__ == "__main__":
    app.run(debug=True)