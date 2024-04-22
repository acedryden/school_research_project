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
import joblib

app = Flask(__name__)

model = joblib.load('grad_prediction_model.joblib')

def serialize_model(model):
    model_params = {
        "intercept": model.intercept_.tolist(),
        "coefficients": model.coef_.tolist()
    }
    return json.dumps(model_params)

 # Define route to serve model JSON
@app.route('/model', methods=['GET'])
def get_model():
     model_json = serialize_model(model)
     return jsonify(model_json)

if __name__ == '__main__':
    app.run(debug=True)
