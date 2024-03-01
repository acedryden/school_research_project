from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, text, inspect, func
from flask import Flask, jsonify, render_template
<<<<<<< Updated upstream

#initiate app
app = Flask(__name__)
=======
from flask_cors import CORS

#initiate app
app = Flask(__name__)
CORS(app)
>>>>>>> Stashed changes

#create engine for postgresql
engine = create_engine("postgresql://project_3_333t_user:3LuhMTGZ77yugy4ExOkIqqROOtWMs4rE@dpg-cnbuglv79t8c73ep52q0-a.ohio-postgres.render.com/project_3_333t", echo=False)
Base = automap_base()
Base.prepare(autoload_with=engine)
enrollment = Base.classes.Enrollment

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

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/api/v1.0/amy_test")
def enroll_chart():
    
    session = Session(engine)
    
<<<<<<< Updated upstream
    sel = [enrollment.School_Number, enrollment.School_Type, enrollment.School_Level,enrollment.Grade_1_Enrolment,enrollment.Grade_2_Enrolment,enrollment.Grade_3_Enrolment, 
             enrollment.Grade_4_Enrolment, enrollment.Grade_5_Enrolment, enrollment.Grade_6_Enrolment, enrollment.Grade_7_Enrolment, enrollment.Grade_8_Enrolment,
             enrollment.Grade_9_Enrolment, enrollment.Grade_10_Enrolment, enrollment.Grade_11_Enrolment, enrollment.Grade_12_Enrolment, enrollment.Total_Enrolment] 
    enr_data= session.query(*sel).all()
    
    school_number = []
    school_type = []
    school_level = []
    gr1 = []
    gr2 = []
    gr3 = []
    gr4 = []
    gr5 = []
    gr6 = []
    gr7 = []
    gr8 = []
    gr9 = []
    gr10 = []
    gr11 = []
    gr12 = []
    gr_total = []
    for record in enr_data: 
        print(record)
        school_number.append(record.School_Number)
        school_type.append(record.School_Type)
        school_level.append(record.School_Level)
        gr1.append(record.Grade_1_Enrolment)
        gr2.append(record.Grade_2_Enrolment)
        gr3.append(record.Grade_3_Enrolment)
        gr4.append(record.Grade_4_Enrolment)
        gr5.append(record.Grade_5_Enrolment)
        gr6.append(record.Grade_6_Enrolment)
        gr7.append(record.Grade_7_Enrolment)
        gr8.append(record.Grade_8_Enrolment)
        gr9.append(record.Grade_9_Enrolment)
        gr10.append(record.Grade_10_Enrolment)
        gr11.append(record.Grade_11_Enrolment)
        gr12.append(record.Grade_12_Enrolment)
        gr_total.append(record.Total_Enrolment)
    
    session.close()
    
    data = {"School Number" : school_number, "School Type" : school_type, "School Level" : school_level, "Grade 1 Enrollment" : gr1, "Grade 2 Enrollment" : gr2,
           "Grade 3 Enrollment" : gr3,"Grade 4 Enrollment" : gr4,"Grade 5 Enrollment" : gr5,"Grade 6 Enrollment" : gr6,"Grade 7 Enrollment" : gr7,
           "Grade 8 Enrollment" : gr8,"Grade 9 Enrollment" : gr9,"Grade 10 Enrollment" : gr10,"Grade 11 Enrollment" : gr11,"Grade 12 Enrollment" : gr12, "Total Enrollment" : gr_total}
    
=======
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

    data = {"elementary_data": ele_data_list, "secondary_data": sec_data_list}


>>>>>>> Stashed changes
    return jsonify(data)

@app.route('/<path:dummy>')
def fallback(dummy):
    return f"404 Not Found: {dummy}"


if __name__ == "__main__":
    app.run(debug=True)


   
