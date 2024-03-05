from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, text, inspect, func
from flask import Flask, jsonify, render_template
from flask_cors import CORS

#initiate app
app = Flask(__name__)
CORS(app)

#create engine for postgresql
engine = create_engine("postgresql://project_3_333t_user:3LuhMTGZ77yugy4ExOkIqqROOtWMs4rE@dpg-cnbuglv79t8c73ep52q0-a.ohio-postgres.render.com/project_3_333t", echo=False)
Base = automap_base()
Base.prepare(autoload_with=engine)
enrollment = Base.classes.Enrollment
school_info = Base.classes.School_info
school_grad = Base.classes.Board_Grad
board_info = Base.classes.Board_info

session = Session(engine)
try:
    
    results = session.query(enrollment).all()
    print('---------------')
    print([x for x in results])
    print('---------------')
except Exception as e: 
    print(f"Error: {e}")
finally: 
    session.close()

CORS(app)
@app.route("/")
def index():
    return render_template('charts.html')

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
    return jsonify(schooldict)

session.close()

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
    ]

    ele_data = (
        session.query(*sel)
        .filter(enrollment.School_Level.in_(['Elementary']))
        .all()
    )

    sec_data = (
        session.query(*sel)
        .filter(enrollment.School_Level.in_(['Secondary']))
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
    
    ele_data_list = [
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
            "Total_Enrolment": record.Total_Enrolment,
        }
        for record in ele_data
    ]
    
    sec_data_list = [
        {
            "School_Number": record.School_Number,
            "Grade_9_Enrolment": record.Grade_9_Enrolment,
            "Grade_10_Enrolment": record.Grade_10_Enrolment,
            "Grade_11_Enrolment": record.Grade_11_Enrolment,
            "Grade_12_Enrolment": record.Grade_12_Enrolment,
            "Total_Enrolment": record.Total_Enrolment,
        }
        for record in sec_data
    ]

    school_info_list = [ 
        {
        "School_Number": record.School_Number, 
        "Board_Number": record.Board_Number, 
        "School_Name" : record.School_Name,
        "School_Level": record.School_Level
        }
        for record in school_info_data
    ]


    data = {"elementary_data": ele_data_list, "secondary_data": sec_data_list, "school_info": school_info_list}


    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)


   
