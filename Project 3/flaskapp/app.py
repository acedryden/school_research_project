import pandas as pd
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, text, inspect, func
from flask import Flask, jsonify, render_template

engine = create_engine("sqlite:///dow.sqlite", echo=False)
Base = automap_base()
Base.prepare(autoload_with=engine)
Dow = Base.classes.dow
app = Flask(__name__)


@app.route("/api/v1.0/dow_data")
def dow_data():
    session = Session(engine)

    sel = [Dow.stock, 
       func.avg(Dow.open_price), 
       func.avg(Dow.high_price), 
       func.avg(Dow.low_price), 
       func.avg(Dow.close_price)]
       
    may_averages = session.query(*sel).\
    filter(func.strftime("%m", Dow.date) == "05").\
    group_by(Dow.stock).\
    order_by(Dow.stock).all()

    stock_names = []
    may_low = [] 
    may_high = []
    for row in may_averages:
        stock_names.append(row[0])
        may_low.append(row[1])
        may_high.append(row[2])

    data = {"names":stock_names, "low":may_low, "high":may_high}
    session.close() 

    return jsonify(data)

@app.route("/")
def welcome():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
