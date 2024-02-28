import pandas as pd
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, text, inspect, func, select, Table, MetaData
from flask import Flask, jsonify, render_template

# engine = create_engine("sqlite:///dow.sqlite", echo=False)


engine = create_engine("postgresql://project_3_333t_user:3LuhMTGZ77yugy4ExOkIqqROOtWMs4rE@dpg-cnbuglv79t8c73ep52q0-a.ohio-postgres.render.com/project_3_333t", echo=False)
Base = automap_base()
Base.prepare(autoload_with=engine)
#Base.classes.keys()
#schools_table = Base.classes.School_Location_2
#school_info = Base.classes.School_Info_2
#session.commit()
Dow = Base.classes.School_Info_2
app = Flask(__name__)

@app.route("/api/v1.0/dow_data")
def dow_data():
    session = Session(engine)
    
    results= session.query(Dow.School_Number, Dow.School_Name).all()
    #for row in data:
       # print(row)
    
    data = dict(results)
    #results2 = session.query(school_info.School_Number, school_info.School_Name).all()
   
    #data = {"names":"my name", "low":2, "high":30}
    session.close() 

    print(data)

    return jsonify(data)

@app.route("/")
def welcome():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
    
#print to get results: http://127.0.0.1:5000//api/v1.0/dow_data
