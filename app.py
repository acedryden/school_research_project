from sqlalchemy import create_engine, text, inspect, func
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base
from flask import Flask, jsonify, render_template
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

# Bord Map variables

elementary = Base.classes.Enrollment
school_info = Base.classes.School_info
board_info = Base.classes.Board_info
board_grad = Base.classes.Board_Grad

# Graph Variables

school_grad = Base.classes.Board_Grad
enrollment = Base.classes.Enrollment

# Main Route


@app.route('/')
def main():

    return render_template('home.html')

### API Routes

# Graduation Table API

@app.route("/api/v0/grad_rate")
def grad_rates():
    session = Session(engine)

    Four_2017_2018 = session.query(board_grad.Four_Year_Graduation_Rate_2017_2018_Grade_9_Cohort , board_info.Municipality ,board_grad.Board_Number ).filter(board_info.Board_Number == board_grad.Board_Number).all()
    Five_2017_2018 = session.query(board_grad.Five_Year_Graduation_Rate_2017_2018_Grade_9_Cohort , board_info.Municipality, board_grad.Board_Number).filter(board_info.Board_Number == board_grad.Board_Number).all()
    Four_2018_2019 = session.query(board_grad.Four_Year_Graduation_Rate_2018_2019_Grade_9_Cohort , board_info.Municipality, board_grad.Board_Number).filter(board_info.Board_Number == board_grad.Board_Number).all()

    data = {}

    for i in range(len(Four_2017_2018)):
        data[(Four_2017_2018[i][2]).upper()] = {}

    for i in range(len(Four_2017_2018)):
        data[Four_2017_2018[i][2]]["Four_2017_2018"] = float(Four_2017_2018[i][0])

    for i in range(len(Five_2017_2018)):
        data[Five_2017_2018[i][2]]["Five_2017_2018"] = float(Five_2017_2018[i][0])

    for i in range(len(Four_2018_2019)):
        data[Five_2017_2018[i][2]]["Four_2018_2019"] = float(Four_2018_2019[i][0])


    session.close()
    return jsonify(data)

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

# Boundries Data Route

@app.route("/api/v0/boundaries.json")
def dmongo():
    objects = bounds.find({},{"_id":False}) 
    return jsonify({"requests": list(objects)})
    
# Graduation Data Route

CORS(app)
@app.route("/api/v1.0/Arti/grad_data")
def dow_data():

    session = Session(engine)
    fiveyear_gradrate = session.query(school_grad.Five_Year_Graduation_Rate_2017_2018_Grade_9_Cohort).all()
    boardnums = session.query(school_grad.Board_Number).all()
    fouryear_gradrate = session.query(school_grad.Four_Year_Graduation_Rate_2017_2018_Grade_9_Cohort).all()
    regions = session.query(school_grad.Region).all()
    fouryear_gradrate2 = session.query(school_grad.Four_Year_Graduation_Rate_2018_2019_Grade_9_Cohort).all()
    boardnames = session.query(board_info.Board_Name).all()
    boardtypes = session.query(board_info.Board_Type).all()

    #data = {"names":"my name", "low":2, "high":30}
    fouryeargrad = [float(row[0]*100) for row in fouryear_gradrate]
    fiveyeargrad = [float(row[0]*100) for row in fiveyear_gradrate]
    board_nums = [row[0] for row in boardnums]
    fouryeargrad2 = [float(row[0]*100) for row in fouryear_gradrate2]
    regions1 = [row[0]for row in regions]
    schoolnames = [row[0] for row in boardnames]
    board_types = [row[0] for row in boardtypes]

    schooldict = {"Board_Names":schoolnames, "Board_Types": board_types, "Board_Numbers":board_nums, "Regions": regions1, "Four_Year_Grads": fouryeargrad, "Five_Year_Grads": fiveyeargrad, "Four_Year_Grads_2019": fouryeargrad2}
    
    session.close()

    return jsonify(schooldict)


# Enrolment Data Route

CORS(app)
@app.route("/api/v1.0/amy_test")
def enroll_chart():
    
    session = Session(engine)
    
    sel = [
        enrollment.School_Number,
        enrollment.Grade_1_Enrolment,
        enrollment.Grade_2_Enrolment,
        enrollment.Grade_3_Enrolment,
        enrollment.Grade_4_Enrolment,
        enrollment.Grade_5_Enrolment,
        enrollment.Grade_6_Enrolment, 
        enrollment.Grade_7_Enrolment,
        enrollment.Grade_8_Enrolment,
        enrollment.Grade_9_Enrolment,
        enrollment.Grade_10_Enrolment,
        enrollment.Grade_11_Enrolment,
        enrollment.Grade_12_Enrolment,
        enrollment.Total_Enrolment,
        school_info.School_Level,  
        school_info.Board_Number,
        school_info.School_Name,
    ]

    enr_data = (
        session.query(*sel)
        .outerjoin(school_info, enrollment.School_Number == school_info.School_Number)
        .all()
    )

    sel_school_info = [ 
        school_info.School_Number, 
        school_info.Board_Number, 
        school_info.School_Name, 
        school_info.School_Level,
    ]

    school_info_data = session.query(*sel_school_info).all()

    session.close()
    
    enr_data_list = [
        {
            "School_Number": record.School_Number,
            "Grade_1_Enrolment": record.Grade_1_Enrolment,
            "Grade_2_Enrolment": record.Grade_2_Enrolment,
            "Grade_3_Enrolment": record.Grade_3_Enrolment,
            "Grade_4_Enrolment": record.Grade_4_Enrolment,
            "Grade_5_Enrolment": record.Grade_5_Enrolment,
            "Grade_6_Enrolment": record.Grade_6_Enrolment,
            "Grade_7_Enrolment": record.Grade_7_Enrolment,
            "Grade_8_Enrolment": record.Grade_8_Enrolment,
            "Grade_9_Enrolment": record.Grade_9_Enrolment,
            "Grade_10_Enrolment": record.Grade_10_Enrolment,
            "Grade_11_Enrolment": record.Grade_11_Enrolment,
            "Grade_12_Enrolment": record.Grade_12_Enrolment,
            "Total_Enrolment": record.Total_Enrolment,
            "School_Level": record.School_Level,
            "Board_Number": record.Board_Number,
            "School_Name": record.School_Name,
        }
        for record in enr_data
    ]
    
    return jsonify({"enr_data": enr_data_list})

@app.route('/api/v1.0/graduation/predicted/<x>.json')
def predicted_enrollment_data(x):
    # Assign the graduation and future graduation to a variable
    Graduation_Data = Base.classes.Board_Grad_2

    # Iniciate Session
    Session = sessionmaker(bind=engine)
    session = Session()

    Graduation_results = session.query(Graduation_Data).all()

    # Extracting the data in the Board_Grad_2 table
    Graduation__Data = [{column.name: str(getattr(result, column.name)) for column in Graduation_Data.__table__.columns} for result in Graduation_results]

    # Closing session
    session.close()

    # Transform the data into Dataframes
    Graduation_df = pd.DataFrame(Graduation__Data)

    # Extracting the first year for each row and transforming to int
    Graduation_df["Year"] = Graduation_df["Year"].astype(str).str.split("-").str[0] 

    # Define the range of future years
    future_years = range(2023, 2027)

    # Create an empty list to store future data
    future_data = []

    # Iterate over each Board
    for Board in Graduation_df['Board_Number'].unique():
        # Filter data for the current Board
        Board_data = Graduation_df[Graduation_df['Board_Number'] == Board]

        # Iterate over each year
        for year in future_years:
            # Create a copy of the last known year's data
            last_year_data = Board_data[Board_data['Year'] == Board_data['Year'].max()].copy()

            # Update the year to the future year
            last_year_data['Year'] = year

            # Append the last year's data with updated year to the future data
            future_data.append(last_year_data)

    # Concatenate the future data into a single DataFrame
    Future_grad_df = pd.concat(future_data, ignore_index=True)

    # Model path
    model_path = "graduation_prediction_model.pkl"

    # Importing the ML model
    with open(model_path, "rb") as f:
        model = pickle.load(f)

        # Selecting only the columns used for prediction
        prediction_features = [col for col in Future_grad_df.columns if col not in ['Region', 'Board_Type', 'Board_Number', 'Four_Year_Graduation_Rate_2018_2019_Grade_9_Cohort']]

        # Making predictions on the Future_grad_df
        predictions = model.predict(Future_grad_df[prediction_features])

    # Importing predictions into Future_grad_df
    Future_grad_df["Four Year Graduation Rate 2017-2018 Grade 9 Cohort"] = predictions

    # Extracting the first year for each row and transforming to int
    Future_grad_df["Year"] = Future_grad_df["Year"].astype(str).str.split("-").str[0]

    # Concatenate Future_grad_df and Graduation_df
    Complete_df = pd.concat([Future_grad_df, Graduation_df], ignore_index=True)

    # Fill NaN values with 0
    Complete_df = Complete_df.fillna(0)

    columns_to_float = ["Credit_Accumulation_by_the_end_of_Grade_10", "Credit_Accumulation_by_the_end_of_Grade_11", 
                        "Four Year Graduation Rate 2017-2018 Grade 9 Cohort", "Four_Year_Graduation_Rate_2018_2019_Grade_9_Cohort",
                        "Grade_10_OSSLT_Results", "Progress_in_Credit_Accumulation_by_the_end_of_Grade_10",
                        "Progress_in_Credit_Accumulation_by_the_end_of_Grade_11", 
                        "Progress_in_Four_Year_Graduation_Rate_2017_2018_Grade_9_Cohort",
                        "Progress_in_Grade_10_OSSLT_Results"]

    Complete_df[columns_to_float] = Complete_df[columns_to_float].astype(float).round(2)

    # Selecting the data for a specific year
    Final_df = Complete_df[Complete_df["Year"] == x]

    # Convert DataFrame back to list of dictionaries
    Complete_Graduations = Final_df.to_dict(orient='records')
    
    data = {}

    board_nums = []
    grad_num = []

    for i in range(len(Complete_Graduations)):
        data[Complete_Graduations[i]["Board_Number"]] = {} 
        board_nums.append(Complete_Graduations[i]["Board_Number"])
        grad_num.append(Complete_Graduations[i]["Four Year Graduation Rate 2017-2018 Grade 9 Cohort"])

    print(board_nums)
    for i in range(len(board_nums)):
        data[board_nums[i]][x] = grad_num[i]

    #print(data)
    # Return the result as JSON
    return jsonify(data)

# School Map Route

@app.route("/map")
def map():
    return render_template('index.html')


@app.route("/enroll_graph")
def enroll_graph():
    return render_template('enroll_graph.html')

@app.route("/API_page")
def API_page():
    return render_template('API_page.html')


@app.route("/grad_graph")
def grad_graph():
    return render_template('grad_graph.html')

@app.route("/board_graph")
def board_graph():
    return render_template('board_graph.html')

# Board Map Route

@app.route("/Graduation_Map")
def website():
    return render_template('grad_rate_map.html')

# Chart Route

@app.route("/graphs")
def index():
    return render_template('charts.html')


# Debugging Function 

if __name__ == "__main__":
    app.run(debug = True)