// // Graduation Plots:
url = '/api/v1.0/Arti/grad_data'
d3.json(url).then(gettingdata);
    
function gettingdata(response){
    // let response = schooldict
    console.log(response);

    var trace1 = {
      x: response.Board_Numbers,
      y: response.Four_Year_Grads,
      text: response.Board_Names,
      
      mode: 'markers',
      marker: {
        size: 10,
        color: "green", 
        opacity: [0.4]
       }
  };
  var trace2 = {
    x: response.Board_Numbers,
    y: response.Four_Year_Grads_2019,
    text: response.Board_Names,
    
    mode: 'markers',
    marker: {
      size: 10,
      color: "blue", 
      opacity: [0.8]
     }
  };

  var trace3 = {
    x: response.Board_Numbers,
    y: response.Five_Year_Grads,
    text: response.Board_Names,
    
    mode: 'markers',
    marker: {
      size: 10 ,
      color: "orange",
      opacity:[0.6] 
     }
  };
  
  var pizza = [trace1,trace2,trace3];
  
  var show = {
      title: 'Rates of Graduation By Board 2021-2022',
      showlegend: false
  };
  
  Plotly.newPlot('plot', pizza, show);

  let info1 = {
    x: response.Regions,
    y: response.Four_Year_Grads,
    text: "%",
    name: "Four Year Graduation Rate 2017-2018 Grade 9 Cohort",
    type: "bar"
  };
  
  // Trace 2 for the 2018-2019 cohort
  let info2 = {
    x: response.Regions,
    y: response.Four_Year_Grads_2019,
    text: "%",
    name: "Four Year Graduation Rate 2018-2019 Grade 9 Cohort",
    type: "bar"
  };

  //
  let info3 = {
    x: response.Regions,
    y: response.Five_Year_Grads,
    text: "%",
    name: "Five Year Graduation Rate 2017-2018 Grade 9 Cohort",
    type: "bar"
  };
  
  // Create data array
  let read = [info1, info2, info3];
  
  // Apply a title to the layout
  let panel = {
    title: "Graduation Rates Across Ontario By Region", 
    xaxis: {automargin: true,}
  };
  
  // Render the plot to the div tag with id "plot"
  Plotly.newPlot("plot3", read, panel);

}
//Enrollment Charts:
document.addEventListener('DOMContentLoaded', function(){
    let enr_data = [{
    values: [357040, 210060, 789530, 427290],
    labels: ['Catholic Elementary', 'Catholic Secondary', 'Public Elementary', 'Public Secondary'],
    type: 'pie'
}];
  
let enr_layout = {
    title: 'Total Enrollments by School Type and Level'
};
  
Plotly.newPlot('enr_pie', enr_data, enr_layout);
});

let top10boards = [
  {"Board Name:" : "Toronto DSB", "Total Enrollment": 193105}, 
  {"Board Name:" :"Peel DSB", "Total Enrollment": 127670},
  {"Board Name:" : "York Region DSB", "Total Enrollment": 105665}, 
  {"Board Name:" : "Toronto CDSB", "Total Enrollment": 83735}, 
  {"Board Name:" : "Ottawa-Carleton DSB", "Total Enrollment": 65020}, 
  {"Board Name:" :"Durham DSB", "Total Enrollment": 63980},
  {"Board Name:" :"Dufferin-Peel CDSB", "Total Enrollment": 62580}, 
  {"Board Name:" : "Halton DSB", "Total Enrollment": 57365},
  {"Board Name:" :"Thames Valley DSB", "Total Enrollment": 55805},
  {"Board Name:" : "Waterloo Region DSB", "Total Enrollment": 53350}
];

let top10boards_data = top10boards.map(entry => entry["Total Enrollment"]).reverse();
let top10boards_labels = top10boards.map(entry => entry["Board Name:"]).reverse(); 

let board_trace = {
  y: top10boards_labels,
  x: top10boards_data,
  type: 'bar', 
  orientation: 'h',
};

let board_layout = {
  title: 'Top 10 District School Boards by Total Enrollment',
  yaxis: { 
  automargin:true, 
  margin: {t:20} },
  xaxis: { title: 'Total Enrollment' }
};

Plotly.newPlot('top_boards', [board_trace], board_layout);



 let top10ele = [
  {"School Name:" : "Gandatsetiagon Public School", "Total Enrollment": 4950}, 
  {"School Name:" : "St Kevin Catholic School", "Total Enrollment": 3720},
  {"School Name:" : "Abbey Lane Public School", "Total Enrollment": 2300}, 
  {"School Name:" : "St. Elizabeth Seton Catholic Elementary School", "Total Enrollment": 2265}, 
  {"School Name:" : "St. David Catholic Elementary School", "Total Enrollment": 2265}, 
  {"School Name:" : "Lackner Woods Public School", "Total Enrollment": 2195},
  {"School Name:" : "St. Francis Xavier Catholic Elementary School", "Total Enrollment": 2165}, 
  {"School Name:" : "St Gregory Catholic Elementary School", "Total Enrollment": 2095},
  {"School Name:" : "Frank Panabaker North School", "Total Enrollment": 1990},
  {"School Name:" : "Queen of Heaven Catholic Elementary School", "Total Enrollment": 1935}
];


let top10ele_data = top10ele.map(entry => entry["Total Enrollment"]).reverse();
let top10ele_labels = top10ele.map(entry => entry["School Name:"]).reverse();

let ele_trace = {
  y: top10ele_labels,
  x: top10ele_data,
  type: 'bar', 
  orientation: 'h',
};

let ele_layout = {
  title: 'Top 10 Elementary Schools by Total Enrollment',
  yaxis: { 
  automargin:true, 
  margin: {t:20} },
  xaxis: { title: 'Total Enrollment' }
};

Plotly.newPlot('top_ele', [ele_trace], ele_layout);

let top10sec = [
  {"School Name:" : "Iroquois Ridge High School", "Total Enrollment": 2030}, 
  {"School Name:" : "G L Roberts Collegiate and Vocational Institute", "Total Enrollment": 1855},
  {"School Name:" : "Sir Frederick Banting Secondary School", "Total Enrollment": 1765}, 
  {"School Name:" : "Peel Alternative North", "Total Enrollment": 1735}, 
  {"School Name:" : "Orillia Secondary School", "Total Enrollment": 1585}, 
  {"School Name:" : "West Credit Secondary School", "Total Enrollment": 1580},
  {"School Name:" : "Langstaff Secondary School", "Total Enrollment": 1565}, 
  {"School Name:" : "Applewood Heights Secondary School", "Total Enrollment": 1505},
  {"School Name:" : "Tommy Douglas Secondary School", "Total Enrollment": 1475},
  {"School Name:" : "Westminster Secondary School", "Total Enrollment": 1465}
];


let top10sec_data = top10sec.map(entry => entry["Total Enrollment"]).reverse();
let top10sec_labels = top10sec.map(entry => entry["School Name:"]).reverse();

let sec_trace = {
  y: top10sec_labels,
  x: top10sec_data,
  type: 'bar', 
  orientation: 'h', 
};

let sec_layout = {
  title: 'Top 10 Secondary Schools by Total Enrollment',
  yaxis: { 
  automargin:true, 
  margin: {t:20} },
  xaxis: { title: 'Total Enrollment' }
};

Plotly.newPlot('top_sec', [sec_trace], sec_layout);

//dynamic charts: 
let selectedSchoolNumber;

function findSchoolInfoByName(schoolName) {
    return school_info.find(item => item['School_Name'] === schoolName);
        }
        document.addEventListener("DOMContentLoaded", function () {
            const apiUrl = "/api/v1.0/amy_test";
            const schoolNameSelector = document.getElementById('schoolNameSelector');
            const schoolInfoDisplay = document.getElementById('schoolInfoDisplay');
        
            fetch(apiUrl)
                .then(response => response.json())
                .then(data => {
                    if (data.enr_data) {
                        school_info = data.enr_data.map(item => ({
                            School_Number: item.School_Number,
                            School_Level: item.School_Level,
                            Board_Number: item.Board_Number,
                            School_Name: item.School_Name,
                        }));
        
                        populateSchoolNamesDropdown(school_info, schoolNameSelector, schoolInfoDisplay);
                        
                        // Set up primary chart only if a school is selected
                        schoolNameSelector.addEventListener('change', function () {
                            const selectedSchoolName = this.value;
                            const selectedSchoolInfo = findSchoolInfoByName(selectedSchoolName);
        
                            if (selectedSchoolInfo) {
                                selectedSchoolNumber = selectedSchoolInfo.School_Number;
                                primarysetupChart('Title', data, selectedSchoolNumber);
                            }
                        });
                    } else {
                        console.error('School info data is missing');
                    }
                })
                .catch(error => {
                    console.error("Error fetching data:", error);
                });
        });
        
function populateSchoolNamesDropdown(schoolNames, schoolNameSelector, schoolInfoDisplay) {
    // Sort schoolNames alphabetically
    schoolNames.sort((a, b) => a.School_Name.localeCompare(b.School_Name));

    // Populate the dropdown with sorted school names
    schoolNames.forEach(item => {
        let option = document.createElement('option');
        option.value = item.School_Name;
        option.text = item.School_Name;
        schoolNameSelector.appendChild(option);
    });
}

function primarysetupChart(title, data, selectedSchoolNumber) {
    console.log('Received data:', data);

    // Check if 'enr_data' is defined
    if (data && selectedSchoolNumber) {
        let flattenedData = data.enr_data.flat();
        let schoolNumbers = flattenedData.map(item => item['School_Number']);

        // Check if schoolNumbers is defined and not empty
        if (schoolNumbers && schoolNumbers.length > 0) {
            // Call the common update function when the school number changes
            const filteredData = filterDataBySchoolNumber(data.enr_data, selectedSchoolNumber);
            updateCharts(["Grade_1_Enrolment", "Grade_2_Enrolment", "Grade_3_Enrolment", "Grade_4_Enrolment", "Grade_5_Enrolment", "Grade_6_Enrolment", "Grade_7_Enrolment", "Grade_8_Enrolment", "Grade_9_Enrolment", "Grade_10_Enrolment", "Grade_11_Enrolment", "Grade_12_Enrolment"], filteredData, 'Primary School', 'primarychart', selectedSchoolNumber);
        } else {
            console.error('School numbers not found or empty');
        }
    } else {
        console.error('Data or selectedSchoolNumber is undefined. Cannot set up chart.');
    }
}
function filterDataBySchoolNumber(data, selectedSchoolNumber) {
    const filteredData = data.filter((item) => {
        const itemSchoolNumber = String(item.School_Number);
        const selectedNumber = String(selectedSchoolNumber);
        const isMatch = itemSchoolNumber === selectedNumber;
        return isMatch;
    });
    return filteredData;
}

function updateCharts(grades, data, title, chartDiv, selectedSchoolNumber) {
    // Check if data and selectedSchoolNumber are defined
        if (!data || !selectedSchoolNumber) {
            console.error('Data or selectedSchoolNumber is undefined. Cannot update chart.');
            console.log('Data:', data);
            console.log('Selected School Number:', selectedSchoolNumber);
            return;
        }
    
        // Replace spaces with underscores in the grades array
        const gradesWithUnderscores = grades.map(grade => grade.replace(/ /g, '_'));
    
        let enrollments = grades.map(grade => {
            // Extract the grade data from the data array
            let gradeData = data[0][grade];
        
            // Check if gradeData is an object and has Total_Enrolment property
            if (typeof gradeData === 'object' && 'Total_Enrolment' in gradeData) {
                return gradeData.Total_Enrolment;
            }
        
            // If not an object or does not have Total_Enrolment property, use the grade data directly
            return gradeData || 0;
        });
    
        // Clear existing chart
        document.getElementById(chartDiv).innerHTML = '';
    
        // Check if enrollments is defined
        if (!enrollments) {
            console.error('Enrollments is undefined. Cannot update chart.');
            return;
        }
    
        // Update chart
        let bartrace = [{
            x: grades,
            y: enrollments,
            type: 'line',
            line: {color: 'rgb(37,134,164)', width: 2},
        }];
    
        let ticktextWithoutUnderscores = gradesWithUnderscores.map(grade => grade.replace(/_/g, ' '));
    
        let layout = {
            title: `Enrollments by Grade - ${title}`,
            xaxis: {
                title: 'Grade',
                tickvals: grades.map((_, index) => index),
                ticktext: ticktextWithoutUnderscores,
            },
            yaxis: { title: '# of Enrollments' }
        };
        Plotly.newPlot(chartDiv, bartrace, layout);
        console.log('Chart updated successfully!');
    }
