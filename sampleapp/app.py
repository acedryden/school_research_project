import requests
from sqlalchemy import create_engine, inspect, func
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base
from flask import Flask, jsonify, render_template

app = Flask(__name__)

engine = create_engine("sqlite:///dow.sqlite", echo=False)
Base = automap_base()
Base.prepare(autoload_with=engine)
Dow = Base.classes.dow

@app.route('/') 
def main(): 
    return render_template("index.html")

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
    for record in may_averages:
        stock_names.append(record[0])
        may_low.append(record[3])
        may_high.append(record[2])

    session.close()

    data = {"names" : stock_names, "low": may_low, "high": may_high}

    return jsonify(data)


# @app.route("/api/v1.0/snp_data")
# def snp_data(): 
#     response = requests.get(url)
#     return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True)