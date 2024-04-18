# Ontario Education Dashboard
## An user-friendly dashboard of interactive maps and graphs exploring Ontario's enrollment and graduation rates of Public and Catholic schools. 

**Team Members:** 
- Alessandro: @AleMori22
- Amy: @acedryden 
- Arti: @Artib03
- Khemaka: @Khemaka14

**Components:** 
1. Landing page including links to school maps, board maps, enrollment and graduation charts, and links to the four data APIs used: ![index](https://github.com/acedryden/school_research_project/blob/main/Output%20Images/dashboard.png)
2. Interactive map that utilizes markets to show the geolocation of individual schools, colour coded by the number of total enrolled students per school: ![school_map](https://github.com/acedryden/school_research_project/blob/main/Output%20Images/school%20map.png)
3. Interactive choropleth map that shows graduation rates on a board level, with a dropdown menu to explore three different sets of graduation data: ![board_map](https://github.com/acedryden/school_research_project/blob/main/Output%20Images/board%20map%20.png)
4. Bubble chart showing the graduation rates by school board for all three data sets, and a summary bar chart showing graduation rates by region for all three data sets: ![grad_charts](https://github.com/acedryden/school_research_project/blob/main/Output%20Images/graduation%20charts%20.png)
5. An exploratory chart where an user can select any school in Ontario and the chart visualizes changes in enrollment levels by grade: ![enr_chart](https://github.com/acedryden/school_research_project/blob/main/Output%20Images/enrollment%20charts.png)
  
**Tools Used:** 
- PostgreSQL and Render Server and MongoDB for data storage and transformation
- QuickDBD for DB Schema
- Flask API
- HTML/CSS
- JavaScript (Plotly, Leaflet)
- Flask-CORS (https://flask-cors.readthedocs.io/en/latest/)
- Tableau for Visualizations Dashboard 

**Links to the datasets:** 
1. https://open.canada.ca/data/dataset/d89271cf-c5b7-4537-9d8b-5905766d93c6
2. https://data.ontario.ca/dataset/school-board-achievements-and-progress
3. https://data.ontario.ca/dataset/school-information-and-student-demographics


