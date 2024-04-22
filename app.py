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
import numpy as np

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

#     # Assign the graduations to a variable 
    Graduation_data = Base.classes.Board_Grad_2

#     # Iniciate Session
    Session = sessionmaker(bind=engine)
    session = Session()

    Graduation_results = session.query(Graduation_data).all()

#     # Extracting the data in the graduation table
    Graduation__data = [{column.name: str(getattr(result, column.name)) for column in Graduation_data.__table__.columns} for result in Graduation_results]

#     # Closing Session 
    session.close()

#     # Trasform the data in to Dataframes
    Graduation_df = pd.DataFrame(Graduation__data)

    grads = np.array(list(Graduation_df))

    grads.reshape(-1,1)

    # Need to fix this

    model = pickle.load(open('graduation_prediction_model.pkl', 'rb'))

    predictions = model.predict(grads)
    print(predictions)

        # Importing predictions in the Future_Enrollment_df
    #Future_Enrollment_df["Total_Enrolment"] = predictions

        # Dimentioning the predicted Total Enrolment as Integer
    #Future_Enrollment_df["Total_Enrolment"] = Future_Enrollment_df["Total_Enrolment"].astype(int)

    # Extracting the first year for each row and transforming to int
    #Enrollment_df["Year"] = Enrollment_df["Year"].astype(str).str.split("-").str[0]    

    # Merge selected columns to Future_Enrollment_df based on School_Number
    #Future_Enrollment_df = Future_Enrollment_df.merge(Enrollment_df[["School_Number", "School_Type", "School_Level"]], on="School_Number", how="left")

    #Complete_df = pd.concat([Enrollment_df])

    # Selecting the data for a specific year
    #Final_df = Complete_df[Complete_df["Year"] == x]

    #Final_df = Final_df.drop_duplicates(subset=["School_Number", "Year"])

    # Convert DataFrame back to list of dictionaries
    #Complete__Enrollment = Final_df.to_dict(orient='records')

    # Return Jsonify Board_data
    return jsonify(predictions)

if __name__ == "__main__":
    app.run(debug=True)
