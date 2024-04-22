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

###predication model for graduate students

#@app.route('/api/v1.0/grad_model')
# @app.route('/')

# def predicted_grad_data():#x):

#     # Assign the graduations to a variable 
#     Graduation_data = Base.classes.Board_Grad_2

#     # Iniciate Session
#     Session = sessionmaker(bind=engine)
#     session = Session()

#     Graduation_results = session.query(Graduation_data).all()

#     # Extracting the data in the graduation table
#     Graduation__data = [{column.name: str(getattr(result, column.name)) for column in Graduation_data.__table__.columns} for result in Graduation_results]

#     # Closing Session 
#     session.close()

#     # Trasform the data in to Dataframes
#     Graduation_df = pd.DataFrame(Graduation__data)

#     grads = np.array(list(Graduation_df))

#     return (grads)

    # Need to fix this
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

model = pickle.load(open('graduation_prediction_model.pkl', 'rb'))

# @app.route('/')
# def home():
#     return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='Employee Salary should be $ {}'.format(output))

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)
