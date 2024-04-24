# Ontario Education Dashboard
An user-friendly dashboard of interactive maps and graphs exploring Ontario's enrollment and graduation rates of Public and Catholic schools, including using linear regression to predict future enrollment and graduation rates. 

## Authors: 
[Alessandro Mori](github.com/AleMori22) <br>
[Amy Dryden](github.com/acedryden) <br>
[Arti Bhatia](github.com/Artib03) <br>
[Khemaka Oo](github.com/Khemaka14)

## Tools Used: 
- QuickDBD for DB Schema
- PostgreSQL, MongoDB and Render Server for data storage and transformation
- Python including Pandas, SciKit-Learn, MatPlotLib, Pickle, SQLAlchemy, PyMongo, PPrint & FlaskCors modules
- Flask API
- HTML/CSS
- JavaScript (Leaflet)
- Tableau Public

## **Components:** 
1. Landing page including links to school maps, board maps, enrollment and graduation charts, and links to the four data APIs and prediction models used: ![index](https://github.com/acedryden/school_research_project/blob/main/Output%20Images/4.22.1.png)
2. Interactive map that utilizes markets to show the geolocation of individual schools, colour coded by the number of total enrolled students per school, and includes: ![school_map](https://github.com/acedryden/school_research_project/blob/main/Output%20Images/school%20map.png)
3. Interactive choropleth map that shows graduation rates on a board level, with a dropdown menu to explore three different sets of graduation data: ![board_map](https://github.com/acedryden/school_research_project/blob/main/Output%20Images/board%20map%20.png)
4. Chart showing the graduation rates by school board for all three graduation periods, and a summary bar chart showing graduation rates by region for all three graduation periods and the Grade 10 OSSLT results: ![grad_dashboard](Output%20Images/Grad%20Dashboard.png)
5. Enrollment dashboard showing School Boards by Enrollments, Top 10 Elemetnary Schools by Enrollments and Top 10 Secondary Schools by Enrollment  ![enr_dashboard](Output%20Images/Enrollment%20Dashboard.png)
6. An exploratory chart where an user can select any school in Ontario and the chart visualizes changes in enrollment levels by grade: ![school_exp](Output%20Images/School%20Board%20Explorer.png)
  
## **Links to the datasets:** 
1. [Ontario Public Schools Enrollment](https://open.canada.ca/data/dataset/d89271cf-c5b7-4537-9d8b-5905766d93c6)
2. [School Boards](https://data.ontario.ca/dataset/school-board-achievements-and-progress)
3. [School Info and Demographics](https://data.ontario.ca/dataset/school-information-and-student-demographics)










