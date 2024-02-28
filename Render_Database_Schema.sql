
CREATE TABLE "School_Location" (
    "School_Number" varchar   NOT NULL,
    "Street" varchar   NOT NULL,
	"Municipality" varchar   NOT NULL,
	"City" varchar   NOT NULL,
	"Province" varchar   NOT NULL,
	"Postal_Code" varchar   NOT NULL,
	"Fax_Number" varchar NOT NULL,
	"Latitude" decimal   NOT NULL,
	"Longitude" decimal  NOT NULL,

    CONSTRAINT "pk_School_Location" PRIMARY KEY (
        "School_Number"
     )
);

CREATE TABLE "School_Info" (
    "School_Number" varchar   NOT NULL,
	"Board_Number" varchar NOT NULL,
	"School_Name" varchar NOT NULL,
	"School_Type" varchar NOT NULL,
	"School_Level" varchar NOT NULL,
	"Phone_Number" varchar NOT NULL,
	"School_Website" varchar NOT NULL,

    CONSTRAINT "pk_School_Info" PRIMARY KEY (
        "School_Number"
     )
);

CREATE TABLE "Elementary_School_Enrolment" (
    "School_Number" varchar NOT NULL,
	"School_Type" varchar NOT NULL,
	"Grade_1_Enrolment" int NOT NULL,
	"Grade_2_Enrolment" int NOT NULL,
	"Grade_3_Enrolment" int NOT NULL,
	"Grade_4_Enrolment" int NOT NULL,
	"Grade_5_Enrolment" int NOT NULL,
	"Grade_6_Enrolment" int NOT NULL,
	"Grade_7_Enrolment" int NOT NULL,
	"Grade_8_Enrolment" int NOT NULL,

    CONSTRAINT "pk_Elementary_School_Enrolment" PRIMARY KEY (
        "School_Number"
     )
);

CREATE TABLE "Secondary_School_Enrolment" (
    "School_Number" varchar NOT NULL,
	"School_Type" varchar NOT NULL,
	"Grade_9_Enrolment" int NOT NULL,
	"Grade_10_Enrolment" int NOT NULL,
	"Grade_11_Enrolment" int NOT NULL,
	"Grade_12_Enrolment" int NOT NULL,


    CONSTRAINT "pk_Secondary_School_Enrolment" PRIMARY KEY (
        "School_Number"
     )
);


--ALTER TABLE "School_Location" ADD CONSTRAINT "fk_School_Location_School_Number" FOREIGN KEY("School_Number")
--REFERENCES "School_Info_2" ("School_Number");
