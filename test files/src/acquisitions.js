const summaryStatsData = [{"School Type":"Catholic","School Level":"Elementary","Total Enrolment":357040},{"School Type":"Catholic","School Level":"Secondary","Total Enrolment":210060},{"School Type":"Protestant Separate","School Level":"Elementary","Total Enrolment":265},{"School Type":"Public","School Level":"Elementary","Total Enrolment":789530},{"School Type":"Public","School Level":"Secondary","Total Enrolment":427290}];
const labels = summaryStatsData.map(entry => `${entry["School Type"]} - ${entry["School Level"]}`);
const dataValues = summaryStatsData.map(entry => entry["Total Enrolment"]);
const data = {
  labels: labels,
  datasets: [{
    label: 'Enrollment by Summary Stats',
    data: dataValues,
    backgroundColor: [
      'rgb(243,169,53)',
      'rgb(199,53,88)',
      'rgb(85,89,106)',
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

// Get the canvas element by ID
const ctx = document.getElementById('acquisitions');

// Create the chart
new Chart(ctx, config);




