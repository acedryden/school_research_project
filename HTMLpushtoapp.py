from sqlalchemy import create_engine, text, inspect, func
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base
from flask import Flask, jsonify, render_template, request
from sqlalchemy.orm import sessionmaker
import json
from pymongo import MongoClient
from pprint import pprint
import pandas as pd
import pickle
from flask_cors import CORS

app = Flask(__name__)

CORS(app)


# Setting up Mongo db

mongo = MongoClient(f"mongodb+srv://khemakaoo:Sr6djqX1vUKxLU7F@cluster0.f5fh96l.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = mongo['Boundary']
bounds = db["Board_bounds"]

# Starting Engine

engine = create_engine("postgresql://project_3_333t_user:3LuhMTGZ77yugy4ExOkIqqROOtWMs4rE@dpg-cnbuglv79t8c73ep52q0-a.ohio-postgres.render.com/project_3_333t", echo=False)
    
# Prepare Base

Base = automap_base()
Base.prepare(engine, reflect=True)

#predication model for graduate students

@app.route('/api/v1.0/graduations_predicted/<x>.json')
def predicted_data(x):


    # Assign the future enrolment to a variable 
    Future_Graduation_Data = Base.classes.
    Graduation_Data = Base.classes.Grad_data_2

    # Iniciate Session
    Session = sessionmaker(bind=engine)
    session = Session()

    Future_Graduation_results = session.query().all()
    Graduation_results = session.query(Graduation_Data).all()

    # Extracting the data in the Enrollment table
    Graduation_Data = [{column.name: str(getattr(result, column.name)) for column in Graduation_Data.__table__.columns} for result in Graduation_results]

    # Extracting the data in the Future_Enrollment table
    Future__Enrollment__data = [{column.name: str(getattr(result, column.name)) for column in Future_Enrollment_Data.__table__.columns} for result in Future_Enrollment_results]
    
    # Closing Session 
    session.close()

    # Trasform the data in to Dataframes
    Enrollment_df = pd.DataFrame(Enrollment__data)
    Future_Enrollment_df = pd.DataFrame(Future__Enrollment__data)

    # Need to fix this

    model_path = "D:\School UFT\school_research_project\enrollment_prediction_model.pkl"

    # Importing the ML model
    with open(model_path, "rb") as f:
        model = pickle.load(f)

        # Making predictions on the Future_Enrollment_df
        predictions = model.predict(Future_Enrollment_df)

        # Importing predictions in the Future_Enrollment_df
        Future_Enrollment_df["Total_Enrolment"] = predictions

        # Dimensioning the predicted Total Enrolment as Integer
        Future_Enrollment_df["Total_Enrolment"] = Future_Enrollment_df["Total_Enrolment"].astype(int)

    # Select only the columns needed from Enrollment_df
    enrollment_columns = Enrollment_df[["Board Number", "Region", "Board Type"]]

    # Merge selected columns to Future_Enrollment_df based on School_Number
    Future_Enrollment_df = pd.merge(, , on="Board Number", how="left")

    Future_Enrollment_df = Future_Enrollment_df[Future_Enrollment_df["Year"] == x]

    # Convert DataFrame back to list of dictionaries
    Future__Enrollment__data = Future_Enrollment_df.to_dict(orient='records')

    # Return Jsonify Board_data
    return jsonify(Future__Enrollment__data)