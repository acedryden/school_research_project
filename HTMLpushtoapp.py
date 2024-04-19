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

import csv
app = Flask(__name__)
CORS(app)

# Setting up Mongo db

mongo = MongoClient(f"mongodb+srv://khemakaoo:Sr6djqX1vUKxLU7F@cluster0.f5fh96l.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = mongo['Boundary']
bounds = db["Board_bounds"]

### Starting Engine

engine = create_engine("postgresql://project_3_333t_user:3LuhMTGZ77yugy4ExOkIqqROOtWMs4rE@dpg-cnbuglv79t8c73ep52q0-a.ohio-postgres.render.com/project_3_333t", echo=False)
    
### Prepare Base

Base = automap_base()
Base.prepare(engine, reflect=True)

###predication model for graduate students

@app.route('/api/v1.0/grad_model')
def predicted_grad_data():#x):

    # Assign the graduations to a variable 
    Graduation_data = Base.classes.Board_Grad_2

    # Iniciate Session
    Session = sessionmaker(bind=engine)
    session = Session()

    Graduation_results = session.query(Graduation_data).all()

    # Extracting the data in the graduation table
    Graduation__data = [{column.name: str(getattr(result, column.name)) for column in Graduation_data.__table__.columns} for result in Graduation_results]

    # Closing Session 
    session.close()

    # Trasform the data in to Dataframes
    Graduation_df = pd.DataFrame(Graduation__data)

    # Need to fix this

    model_path = 'graduation_prediction_model.pkl'

    # Importing the ML model
    with open(model_path, "rb") as f:
        model = pickle.load(f)

        # Making predictions on the Future_grad_df
        predictions = model.predict(Future_grad_df)

        # Importing predictions 
        Future_grad_df["Four Year Graduation Rate 2017-2018 Grade 9 Cohort"] = predictions

        # Dimentioning the predicted 
        Future_grad_df["Four Year Graduation Rate 2017-2018 Grade 9 Cohort"] = Future_grad_df["Four Year Graduation Rate 2017-2018 Grade 9 Cohort"].astype(float)

    # Extracting the first year for each row and transforming to int
    Graduation_df["Year"] = Graduation_df["Year"].astype(str).str.split("-").str[0]    

    # Merge selected columns to Future_Enrollment_df based on Board_number
    Future_grad_df = Future_grad_df.merge(Graduation_df[["Board Number", "Region", "Board Type"]], on="Board Number", how="left")

    Complete_df = pd.concat([Graduation_df])#Future_grad_df])

    # Selecting the data for a specific year
    #Final_df = Complete_df[Complete_df["Year"] == x]

    #Final_df = Final_df.drop_duplicates(subset=["Boad Number", "Year"])

    # Convert DataFrame back to list of dictionaries
    Complete__grads = Complete_df.to_dict(orient='records')

    # Return Jsonify Board_data
    return jsonify(Complete__grads)

if __name__ == "__main__":
    app.run(debug=True)
