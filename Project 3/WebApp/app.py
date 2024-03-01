import pandas as pd
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, text, inspect, func, select, Table, MetaData
from flask import Flask, jsonify, render_template

# engine = create_engine("sqlite:///dow.sqlite", echo=False)


engine = create_engine("postgresql://project_3_333t_user:3LuhMTGZ77yugy4ExOkIqqROOtWMs4rE@dpg-cnbuglv79t8c73ep52q0-a.ohio-postgres.render.com/project_3_333t", echo=False)
Base = automap_base()
Base.prepare(autoload_with=engine)
school_grad = Base.classes.Board_Grad
#Base.classes.keys()
#session.commit()

app = Flask(__name__)

@app.route("/api/v1.0/Arti/grad_data")
def dow_data():
    session = Session(engine)
    fiveyear_gradrate = session.query(school_grad.Five_Year_Graduation_Rate_2017_2018_Grade_9_Cohort).all()
    boardnums = session.query(school_grad.Board_Number).all()
    fouryear_gradrate = session.query(school_grad.Four_Year_Graduation_Rate_2017_2018_Grade_9_Cohort).all()
    regions = session.query(school_grad.Region).all()
    fouryear_gradrate2 = session.query(school_grad.Four_Year_Graduation_Rate_2018_2019_Grade_9_Cohort).all()

    #data = {"names":"my name", "low":2, "high":30}
    fouryeargrad = [float(row[0]*100) for row in fouryear_gradrate]
    fiveyeargrad = [float(row[0]*100) for row in fiveyear_gradrate]
    board_nums = [row[0] for row in boardnums]
    fouryeargrad2 = [float(row[0]*100) for row in fouryear_gradrate2]
    regions1 = [row[0]for row in regions]

    schooldict = {"Board_Numbers":board_nums, "Regions": regions1, "Four_Year_Grads": fouryeargrad, "Five_Year_Grads": fiveyeargrad, "Four_Year_Grads_2019": fouryeargrad2}

    return jsonify(schooldict)

    sesssion.close()

@app.route("/")
def welcome():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
    
#print to get results: http://127.0.0.1:5000/api/v1.0/Arti/grad_data
