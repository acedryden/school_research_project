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
    return render_template('index.html')

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

CORS(app)
@app.route('/<path:dummy>')
def fallback(dummy):
    return f"404 Not Found: {dummy}"


if __name__ == "__main__":
    app.run(debug=True)


   
