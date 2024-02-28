from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base
from flask import Flask, jsonify, render_template
from sqlalchemy.orm import sessionmaker
import json


import pandas as pd

app = Flask(__name__)

#engine = create_engine("postgresql://project_3_333t_user:3LuhMTGZ77yugy4ExOkIqqROOtWMs4rE@dpg-cnbuglv79t8c73ep52q0-a.ohio-postgres.render.com/project_3_333t", echo=False)

#Base = automap_base()
#Base.prepare(engine, reflect=True)

#School_Location = Base.classes.School_Location_2


# Main Route

@app.route('/')
def main():

    return render_template('home.html')

    
# Map Route

@app.route("/map")
def map():
    return render_template('index.html')

# Debugging Function 

if __name__ == "__main__":
    app.run(debug = True)