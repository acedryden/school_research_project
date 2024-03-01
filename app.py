from sqlalchemy import create_engine, inspect 
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base
from flask import Flask, jsonify, render_template
from sqlalchemy.orm import sessionmaker
import json


import pandas as pd

app = Flask(__name__)

# Starting Engine

engine = create_engine("postgresql://project_3_333t_user:3LuhMTGZ77yugy4ExOkIqqROOtWMs4rE@dpg-cnbuglv79t8c73ep52q0-a.ohio-postgres.render.com/project_3_333t", echo=False)
    
# Prepare Base

Base = automap_base()
Base.prepare(engine, reflect=True)

# Main Route

@app.route('/')
def main():

    return render_template('home.html')

### API Routes

# School Data Route

@app.route('/api/v1.0/school/info.json')
def get_school_data():

    # Assign the School_info table to a variable

    School_info_Data = Base.classes.School_info

    # Iniciate Session

    Session = sessionmaker(bind=engine)
    session = Session()

    # Query School_info_Data

    School_results = session.query(School_info_Data).all()

    # Extracting the data in the School_info table

    School_data = []

    for result in School_results:
        record = {column.name: str(getattr(result, column.name)) for column in School_info_Data.__table__.columns}
        School_data.append(record)

    session.close()

    # Return Jsonify School_data

    return jsonify(School_data)


# Board Data Route

@app.route('/api/v1.0/board/info.json')
def get_board_data():

    # Assign the Board_info table to a variable
    
    Board_info_Data = Base.classes.Board_info

    # Iniciate Session

    Session = sessionmaker(bind=engine)
    session = Session()

    # Query Board_info_Data

    Board_results = session.query(Board_info_Data).all()

    # Extracting the data in the Board_info table

    Board_data = []

    for result in Board_results:
        record = {column.name: str(getattr(result, column.name)) for column in Board_info_Data.__table__.columns}
        Board_data.append(record)

    session.close()

    # Return Jsonify Board_data

    return jsonify(Board_data)


# Board Graduation Data Route

@app.route('/api/v1.0/board/grad.json')
def get_graduation_data():

    # Assign the Board_Grad table to a variable
    
    Board_graduation_Data = Base.classes.Board_Grad

    # Iniciate Session

    Session = sessionmaker(bind=engine)
    session = Session()

    # Query Board_graduation_Data

    Board_grad_results = session.query(Board_graduation_Data).all()

    # Extracting the data in the Board_Grad table

    Board_grad_data = []

    for result in Board_grad_results:
        record = {column.name: str(getattr(result, column.name)) for column in Board_graduation_Data.__table__.columns}
        Board_grad_data.append(record)

    session.close()

    # Return Jsonify Board_grad_data

    return jsonify(Board_grad_data)


# Enrollment Data Route

@app.route('/api/v1.0/enrollment.json')
def get_enrollment_data():

    # Assign the Enrollment table to a variable
    
    Enrollment_Data = Base.classes.Enrollment

    # Iniciate Session

    Session = sessionmaker(bind=engine)
    session = Session()

    # Query Enrollment_Data

    Enrollment_results = session.query(Enrollment_Data).all()

    # Extracting the data in the Enrollment table

    Enrollment__data = []

    for result in Enrollment_results:
        record = {column.name: str(getattr(result, column.name)) for column in Enrollment_Data.__table__.columns}
        Enrollment__data.append(record)

    session.close()

    # Return Jsonify Board_data

    return jsonify(Enrollment__data)

    
# Map Test Route

@app.route("/map")
def map():
    return render_template('index.html')

# Debugging Function 

if __name__ == "__main__":
    app.run(debug = True)