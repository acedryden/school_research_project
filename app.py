import pandas as pd
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, text, inspect, func
from flask import Flask, jsonify, render_template

engine = create_engine("postgresql://project_3_333t_user:3LuhMTGZ77yugy4ExOkIqqROOtWMs4rE@dpg-cnbuglv79t8c73ep52q0-a.ohio-postgres.render.com/project_3_333t", echo=False)
Base = automap_base()
Base.prepare(autoload_with=engine)
school_location = Base.classes.School_Info_2
app = Flask(__name__)


@app.route("/")
def dow_data():
    return ("hello")


@app.route("/site")
def website():
    return render_template('index.html')

@app.route("/v0")
def welcome():
    session = Session(engine)
    schoolnums = session.query(school_location.School_Number).limit(5).all()
    boardnums = session.query(school_location.Board_Number).limit(5).all()

    school_num = [row[0] for row in schoolnums]
    board_num = [row[0] for row in boardnums]
    data = {"School Number" : school_num, "Board Number" : board_num}
    print(data)
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)