import pandas as pd
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, text, inspect, func
from flask import Flask, jsonify, render_template

from project_pass import pas

from pymongo import MongoClient
from pprint import pprint
import pandas as pd

mongo = MongoClient(f"mongodb+srv://khemakaoo:{pas}@cluster0.f5fh96l.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = mongo['Boundary']
bounds = db["asd"]

engine = create_engine("postgresql://project_3_333t_user:3LuhMTGZ77yugy4ExOkIqqROOtWMs4rE@dpg-cnbuglv79t8c73ep52q0-a.ohio-postgres.render.com/project_3_333t", echo=False)
Base = automap_base()
Base.prepare(autoload_with=engine)
elementary = Base.classes.Enrollment
school_info = Base.classes.School_info
board_info = Base.classes.Board_info
board_grad = Base.classes.Board_Grad
app = Flask(__name__)


@app.route("/")
def dow_data():
    return render_template('Jumbo.html')

@app.route("/api/v0/grad_rate")
def grad_rates():
    session = Session(engine)

    Four_2017_2018 = session.query(board_grad.Four_Year_Graduation_Rate_2017_2018_Grade_9_Cohort , board_info.Municipality ,board_grad.Board_Number ).filter(board_info.Board_Number == board_grad.Board_Number).all()
    Five_2017_2018 = session.query(board_grad.Five_Year_Graduation_Rate_2017_2018_Grade_9_Cohort , board_info.Municipality, board_grad.Board_Number).filter(board_info.Board_Number == board_grad.Board_Number).all()
    Four_2018_2019 = session.query(board_grad.Four_Year_Graduation_Rate_2018_2019_Grade_9_Cohort , board_info.Municipality, board_grad.Board_Number).filter(board_info.Board_Number == board_grad.Board_Number).all()

    data = {}

    for i in range(len(Four_2017_2018)):
        data[(Four_2017_2018[i][1]).upper()] = {}


    for i in range(len(Four_2017_2018)):
        data[(Four_2017_2018[i][1]).upper()][Four_2017_2018[i][2]] = {}

    for i in range(len(Four_2017_2018)):
        data[(Four_2017_2018[i][1]).upper()][Four_2017_2018[i][2]]["Four_2017_2018"] = float(Four_2017_2018[i][0])

    for i in range(len(Five_2017_2018)):
        data[(Four_2017_2018[i][1]).upper()][Five_2017_2018[i][2]]["Five_2017_2018"] = float(Five_2017_2018[i][0])

    for i in range(len(Four_2018_2019)):
        data[(Four_2017_2018[i][1]).upper()][Five_2017_2018[i][2]]["Four_2018_2019"] = float(Four_2018_2019[i][0])


    session.close()
    return jsonify(data)

@app.route("/mongo")
def dmongo():
    objects = bounds.find({},{"_id":False}) 
    return jsonify({"requests": list(objects)})

@app.route("/site")
def website():
    return render_template('index.html')


# @app.route("/idk")
# def school_map():
#     session = Session(engine)

#     school_lat = session.query(school_info.Latitude).all()
#     school_long = session.query(school_info.Longitude).all()

#     school_lat_list = [float(row[0]) for row in school_lat]
#     school_long_list = [float(row[0]) for row in school_long]

#     data = {"Latitude" : school_lat_list, "Longitude" : school_long_list}

#     session.close()
#     return jsonify(data)

# @app.route("/v0")
# def welcome():
#     session = Session(engine)

#     schoolnums = session.query(elementary.School_Number).all()
#     grade8 = session.query(elementary.Grade_8_Enrolment).all()

#     school_num = [row[0] for row in schoolnums]
#     grade_8 = [row[0] for row in grade8]

#     data = {"School_Number" : school_num, "Grade_8_Enrolment" : grade_8}
    
#     session.close()
#     return jsonify(data)

@app.route("/close")
def wewb():
    return render_template('test.html')

if __name__ == "__main__":
    app.run(debug=True)