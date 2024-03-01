document.addEventListener('DOMContentLoaded', function () {
    console.log("DOM content loaded");
    const url = '/api/v1.0/amy_test';

    function fetchDataAndUpdateUI() {
        d3.json(url)
            .then(data => {
                // Log the data to check its structure
                console.log('Loaded Data:', data);
    
                // Check if data is an object
                if (typeof data === 'object' && !Array.isArray(data)) {
                    // Extract the arrays from the object
                    let primaryData = data['Grade 1 Enrollment'];
                    let secondaryData = data['Grade 2 Enrollment'];

                    console.log('Primary Data:', primaryData);
                    console.log('Secondary Data:', secondaryData);
    
                    if (primaryData && primaryData.length > 0) {
                        primarysetupChart('Primary Schools', primaryData);
                    } else {
                        console.error('Primary data not found');
                    }
    
                    if (secondaryData && secondaryData.length > 0) {
                        secondarysetupChart('Secondary Schools', secondaryData);
                    } else {
                        console.error('Secondary data not found');
                    }
                } else {
                    console.error('Data is not an object');
                }
            })
            .catch(error => {
                console.error('Error fetching data:', error);
            });
    }
    

    // Fetch data and update UI on DOMContentLoaded
    fetchDataAndUpdateUI();

    // Helper functions (getUniqueSchoolNumbers, populateSchoolDropdown, filterDataBySchoolNumber, updateChart) remain the same
});

//function filterDataBySchoolNumber(data, selectedIndex) {
    //if (selectedIndex >= 0 && selectedIndex < data['School Level'].length) {
        //let keys = Object.keys(data);
       //let filteredData = {};
        //keys.forEach(key => {
            //filteredData[key] = data[key][selectedIndex];
        //});
        //return filteredData;
    //} else {
        //console.error('Invalid selectedIndex:', selectedIndex);
        //return null; // or handle the error in an appropriate way
    //}
//}


//const primaryData = filterDataBySchoolLevel(data, 'Elementary');
//const secondaryData = filterDataBySchoolLevel(data, 'Secondary');


//function getUniqueSchoolNumbers(schoolNumbers) {
    //return Array.from(new Set(schoolNumbers));
//}

//function populateSchoolDropdown(schoolNumbers) {
    //let dropdown = document.getElementById('schoolSelector');

    //if (schoolNumbers && schoolNumbers.length > 0) {
        //schoolNumbers.forEach(schoolNumber => {
            //let option = document.createElement('option');
            //option.value = schoolNumber;
            //option.text = schoolNumber;
            //dropdown.appendChild(option);
        //});
    //} else {
        //console.error('School numbers not found or empty');
    //}
//}

function filterDataBySchoolNumber(data, selectedIndex) {
    let keys = Object.keys(data);
    let filteredData = {};
    keys.forEach(key => {
        filteredData[key] = data[key][selectedIndex];
    });
    return filteredData;
}

let selectedSchoolNumber = null;

function primarysetupChart(title, data) {
    let schoolNumbers = filterDataBySchoolLevel(data, 'Elementary').map(item => item['School Number']);

    // Check if schoolNumbers is defined and not empty
    if (schoolNumbers && schoolNumbers.length > 0) {
        console.log('School Numbers:', schoolNumbers);

        document.getElementById('schoolSelector').addEventListener('change', function () {
            selectedSchoolNumber = this.value;
            // Call the common update function when school number changes
            updateCharts(["Grade 1", "Grade 2", "Grade 3", "Grade 4", "Grade 5", "Grade 6", "Grade 7", "Grade 8"], data, title, 'primarychart');
        });

        // Initial chart setup
        updateCharts(["Grade 1", "Grade 2", "Grade 3", "Grade 4", "Grade 5", "Grade 6", "Grade 7", "Grade 8"], data, title, 'primarychart');
    } else {
        console.error('School numbers not found or empty');
    }
}


function secondarysetupChart(title, data) {
    let schoolNumbers = data["School Level"] === "Secondary" ? data["School Number"] : null;

    // Check if schoolNumbers is defined and not empty
    if (schoolNumbers && schoolNumbers.length > 0) {
        console.log('School Numbers:', schoolNumbers);

        document.getElementById('schoolSelector').addEventListener('change', function () {
            // Call the common update function when school number changes
            updateCharts(["Grade 9", "Grade 10", "Grade 11", "Grade 12"], data, title, 'secondarychart');
        });

        // Initial chart setup
        updateCharts(["Grade 9", "Grade 10", "Grade 11", "Grade 12"], data, title, 'secondarychart');
    } else {
        console.error('School numbers not found or empty');
    }
}

function updateCharts(grades, data, title, chartDiv) {
    console.log(`Updating ${title} chart...`);
    console.log('Selected School Number:', selectedSchoolNumber);
    console.log('Data:', data);

    // Extract grade enrollments from filteredData
    let enrollments = grades.map(grade => data[`${grade} Enrollment`]);

    console.log('Enrollments:', enrollments);

    // Check and log undefined enrollment values
    let undefinedEnrollments = enrollments.reduce((undefinedIndices, val, index) => {
        if (typeof val === 'undefined') {
            undefinedIndices.push(index);
        }
        return undefinedIndices;
    }, []);

    console.log('Undefined Enrollments:', undefinedEnrollments);

    if (undefinedEnrollments.length === 0) {
        // Clear existing chart
        document.getElementById(chartDiv).innerHTML = '';

        let bartrace = [{
            x: grades,
            y: enrollments,
            type: 'line',
            line: {color: 'rgb(37,134,164)', width: 2},
        }];

        let layout = {
            title: `Enrollments by Grade - ${title}`,
            xaxis: { title: 'Grade' },
            yaxis: { title: '# of Enrollments' }
        };

        console.log('Creating new plot with data:', bartrace, 'and layout:', layout);

        Plotly.newPlot(chartDiv, bartrace, layout);
        console.log('Chart updated successfully!');
    } else {
        console.error('Some enrollment values are undefined at indices:', undefinedEnrollments);
    }
}





