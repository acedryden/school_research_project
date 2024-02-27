import pandas as pd
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, text, inspect, func, select, Table, MetaData
from flask import Flask, jsonify, render_template

# engine = create_engine("sqlite:///dow.sqlite", echo=False)

engine = create_engine("postgresql://project_3_333t_user:3LuhMTGZ77yugy4ExOkIqqROOtWMs4rE@dpg-cnbuglv79t8c73ep52q0-a.ohio-postgres.render.com/project_3_333t", echo=False)
Base = automap_base()
Base.prepare(autoload_with=engine)
Dow = Base.classes.School_Info
app = Flask(__name__)

@app.route("/api/v1.0/dow_data")
def dow_data():
    session = Session(engine)

    data = {"names":"my name", "low":2, "high":30}
    session.close() 

    print(data)

    return jsonify(data)

@app.route("/")
def welcome():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
    

