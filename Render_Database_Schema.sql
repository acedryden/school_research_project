
CREATE TABLE "Board_info" (
    "Board_Number" varchar,
    "Board_Name" varchar,
    "Board_Type" varchar ,
    "Municipality" varchar ,
    "Board_Website" varchar,
    CONSTRAINT "pk_Board_info" PRIMARY KEY (
        "Board_Number"
     )
);

CREATE TABLE "School_info" (
    "School_Number" int ,
    "Board_Number" varchar ,
    "School_Name" varchar  ,
    "School_Type" varchar ,
    "School_Level" varchar ,
    "Street" varchar    ,
    "Municipality" varchar    ,
    "City" varchar    ,
    "Province" varchar   ,
    "Postal_Code" varchar  ,
	"Fax_Number" varchar,
    "Latitude" decimal  ,
    "Longitude" decimal  ,
    "Phone_Number" varchar   ,
    "School_Website" varchar   ,
    CONSTRAINT "pk_School_info" PRIMARY KEY (
        "School_Number"
     )
);

CREATE TABLE "Board_Grad" (
    "Board_Number" varchar ,
    "Year" varchar ,
    "Region" varchar ,
    "Progress_in_Grade_10_OSSLT_Results" decimal ,
    "Four_Year_Graduation_Rate_2017_2018_Grade_9_Cohort" decimal,
    "Progress_in_Four_Year_Graduation_Rate_2017_2018_Grade_9_Cohort" decimal  ,
    "Five_Year_Graduation_Rate_2017_2018_Grade_9_Cohort" decimal,
    "Progress_in_Five_Year_Graduation_Rate_2017_2018_Grade_9_Cohort" decimal ,
    "Four_Year_Graduation_Rate_2018_2019_Grade_9_Cohort" decimal  ,
    "Progress_in_Four_Year_Graduation_Rate_2018_2019_Grade_9_Cohort" decimal  ,
    CONSTRAINT "pk_Board_Grad" PRIMARY KEY (
        "Board_Number","Year"
     )
);

CREATE TABLE "Enrollment" (
    "School_Number" int ,
    "Year" varchar ,
    "School_Type" varchar ,
    "School_Level" varchar ,
    "Grade_1_Enrolment" int ,
    "Grade_2_Enrolment" int  ,
    "Grade_3_Enrolment" int ,
    "Grade_4_Enrolment" int ,
    "Grade_5_Enrolment" int ,
    "Grade_6_Enrolment" int ,
    "Grade_7_Enrolment" int  ,
    "Grade_8_Enrolment" int ,
    "Grade_9_Enrolment" int ,
    "Grade_10_Enrolment" int ,
    "Grade_11_Enrolment" int ,
    "Grade_12_Enrolment" int  ,
    "Total_Enrolment" int  ,
    CONSTRAINT "pk_Enrollment" PRIMARY KEY (
        "School_Number","Year"
     )
);

ALTER TABLE "School_info" ADD CONSTRAINT "fk_School_info_Board_Number" FOREIGN KEY("Board_Number")
REFERENCES "Board_info" ("Board_Number");

ALTER TABLE "Board_Grad" ADD CONSTRAINT "fk_Board_Grad_Board_Number" FOREIGN KEY("Board_Number")
REFERENCES "Board_info" ("Board_Number");

ALTER TABLE "Enrollment" ADD CONSTRAINT "fk_Enrollment_School_number" FOREIGN KEY("School_Number")
REFERENCES "School_info" ("School_Number");

