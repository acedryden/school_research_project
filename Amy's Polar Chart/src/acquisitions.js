const enr_summaryStatsData = [{"School Type":"Catholic","School Level":"Elementary","Total Enrolment":357040}
,{"School Type":"Catholic","School Level":"Secondary","Total Enrolment":210060}
,{"School Type":"Public","School Level":"Elementary","Total Enrolment":789530}
,{"School Type":"Public","School Level":"Secondary","Total Enrolment":427290}];
const labels = enr_summaryStatsData.map(entry => `${entry["School Type"]} - ${entry["School Level"]}`);
const dataValues = enr_summaryStatsData.map(entry => entry["Total Enrolment"]);
const data = {
  labels: labels,
  datasets: [{
    label: 'Enrollment by Summary Stats',
    data: dataValues,
    backgroundColor: [
      'rgb(243,169,53)',
      'rgb(199,53,88)',
      'rgb(110,190,159)',
      'rgb(37,134,164)'
    ]
  }]
};

const config = {
  type: 'polarArea',
  data: data,
  options: {}
};

//Get the canvas element by ID
const ctx = document.getElementById('acquisitions');

//Create the chart
new Chart(ctx, config);

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
  marker:{ 
  color:'rgb(110,190,159)'}
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
  marker: { 
  color:'rgb(199,53,88)'}
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
  marker: {
    color: 'rgb(243,169,53)'
  }
};

let sec_layout = {
  title: 'Top 10 Secondary Schools by Total Enrollment',
  yaxis: { 
  automargin:true, 
  margin: {t:20} },
  xaxis: { title: 'Total Enrollment' }
};

Plotly.newPlot('top_sec', [sec_trace], sec_layout);

