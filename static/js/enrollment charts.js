let sample_data = {School_Number: 19186, 
Grade_1_Enrollment:20, 
Grade_2_Enrollment:40, 
Grade_3_Enrollment:30, 
Grade_4_Enrollment:25, 
Grade_5_Enrollment:20, 
Grade_6_Enrollment:30, 
Grade_7_Enrollment:15, 
Grade_8_Enrollment:25}

let grades = Object.keys(sample_data).filter(key => key.includes('Grade_'));
let enrollments = grades.map(grade => sample_data[grade]);

let bartrace = {
    x: grades, 
    y: enrollments, 
    type: 'bar', 
    text: enrollments.map(String), 
    textposition: 'auto', 
    hoverinfo: 'y+text', 
}

let layout = {
    title: 'Enrollments by Grade', 
    xaxis: {title: 'Grade'}, 
    yaxis: {title: 'Enrollment'}, 

};

let data = [bartrace]; 

Plotly.newPlot('myDiv', data, layout); 