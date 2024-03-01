let selectedPrimarySchoolNumber = null;
let selectedSecondarySchoolNumber = null;

document.addEventListener("DOMContentLoaded", function () {
    console.log('DOM Content Loaded');
    const apiUrl = "http://localhost:5000/api/v1.0/amy_test";

    fetch(apiUrl)
        .then(response => response.json())
        .then(data => {
            populateSchoolDropdown(data.elementary_data.map(item => item['School_Number']), 'primarySchoolSelector');
            populateSchoolDropdown(data.secondary_data.map(item => item['School_Number']), 'secondarySchoolSelector');
            console.log('Fetched Data:', data);

            // Setup primary chart after data is fetched
            primarysetupChart('Title', data);

            secondarysetupChart('Secondary Title', data);

        })
        .catch(error => {
            console.error("Error fetching data:", error);
        });
});

function primarysetupChart(title, data) {
    console.log('Inside primarysetupChart');
    
    let schoolNumbers = data.elementary_data.map(item => item['School_Number']);

    // Check if schoolNumbers is defined and not empty
    if (schoolNumbers && schoolNumbers.length > 0) {
        console.log('School Numbers:', schoolNumbers);

        const primarySchoolSelector = document.getElementById('primarySchoolSelector');
        
        // Clear existing options in the dropdown
        primarySchoolSelector.innerHTML = '';

        // Populate the dropdown with all available schools
        populateSchoolDropdown(schoolNumbers, 'primarySchoolSelector');

        primarySchoolSelector.addEventListener('change', function () {
            selectedPrimarySchoolNumber = this.value;
            console.log('Primary School Selector changed. Selected School Number:', selectedPrimarySchoolNumber);

            // Call the common update function when school number changes
            const filteredData = filterDataBySchoolNumber(data.elementary_data, selectedPrimarySchoolNumber);
            console.log('Filtered Data:', filteredData);
            updateCharts(["Grade_1_Enrolment", "Grade_2_Enrolment", "Grade_3_Enrolment", "Grade_4_Enrolment", "Grade_5_Enrolment", "Grade_6_Enrolment", "Grade_7_Enrolment", "Grade_8_Enrolment"], filteredData, 'Primary School', 'primarychart', selectedPrimarySchoolNumber);
        });

        // Initial chart setup
        updateCharts(["Grade_1_Enrolment", "Grade_2_Enrolment", "Grade_3_Enrolment", "Grade_4_Enrolment", "Grade_5_Enrolment", "Grade_6_Enrolment", "Grade_7_Enrolment", "Grade_8_Enrolment"], data.elementary_data, 'Primary School', 'primarychart', selectedPrimarySchoolNumber);
    } else {
        console.error('School numbers not found or empty');
    }
}

function filterDataBySchoolNumber(data, selectedSchoolNumber) {
    console.log("Inside filterDataBySchoolNumber");
    console.log("Selected School Number:", selectedSchoolNumber);

    const filteredData = data.filter((item) => {
        console.log("Item:", item);
  
        const itemSchoolNumber = String(item.School_Number);
        const selectedNumber = String(selectedSchoolNumber);
  
        console.log("Item School Number:", itemSchoolNumber);
        console.log("Trimmed Selected School Number:", selectedNumber);
  
        const isMatch = itemSchoolNumber === selectedNumber;
        console.log("Is Match:", isMatch);
  
        return isMatch;
    });

    console.log("Filtered Data:", filteredData);
    return filteredData;
}

function populateSchoolDropdown(schoolNumbers, dropdownId) {
    console.log('Inside populateSchoolDropdown')
    let dropdown = document.getElementById(dropdownId);

    if (schoolNumbers && schoolNumbers.length > 0) {
        schoolNumbers.forEach(schoolNumber => {
            let option = document.createElement('option');
            option.value = schoolNumber;
            option.text = schoolNumber;
            dropdown.appendChild(option);
        });

        console.log(`Populating Primary Dropdown with ${schoolNumbers.length} schools.`);
    } else {
        console.error('School numbers not found or empty');
    }
}

function secondarysetupChart(title, data) {
    console.log('Inside secondarysetupChart');
    
    let schoolNumbers = data.secondary_data.map(item => item['School_Number']);

    // Check if schoolNumbers is defined and not empty
    if (schoolNumbers && schoolNumbers.length > 0) {
        console.log('School Numbers:', schoolNumbers);

        const secondarySchoolSelector = document.getElementById('secondarySchoolSelector');
        
        // Clear existing options in the dropdown
        secondarySchoolSelector.innerHTML = '';

        // Populate the dropdown with all available schools
        populateSchoolDropdown(schoolNumbers, 'secondarySchoolSelector');

        secondarySchoolSelector.addEventListener('change', function () {
            selectedSecondarySchoolNumber = this.value;
            console.log('Secondary School Selector changed. Selected School Number:', selectedSecondarySchoolNumber);

            // Call the common update function when school number changes
            const filteredData = filterDataBySchoolNumber(data.secondary_data, selectedSecondarySchoolNumber);
            console.log('Filtered Data:', filteredData);
            console.log('Grades for Secondary Chart:', ["Grade 9", "Grade 10", "Grade 11", "Grade 12"]);
            console.log('Filtered Data for Secondary Chart:', filteredData);

            updateCharts(["Grade_9_Enrolment", "Grade_10_Enrolment", "Grade_11_Enrolment", "Grade_12_Enrolment"], filteredData, 'Secondary School', 'secondarychart', selectedSecondarySchoolNumber);
        });


        // Initial chart setup
        updateCharts(["Grade_9_Enrolment", "Grade_10_Enrolment", "Grade_11_Enrolment", "Grade_12_Enrolment"], data.secondary_data, 'Secondary School', 'secondarychart', selectedSecondarySchoolNumber);
    } else {
        console.error('School numbers not found or empty');
    }
}

function updateCharts(grades, data, title, chartDiv, selectedSchoolNumber) {
    console.log(`Updating ${title} chart...`);
    console.log('Selected School Number:', selectedSchoolNumber);
    console.log('Data:', data);

    // Check if data and selectedSchoolNumber are defined
    if (!data || !selectedSchoolNumber) {
        console.error('Data or selectedSchoolNumber is undefined. Cannot update chart.');
        return;
    }

    // Replace spaces with underscores in the grades array
    const gradesWithUnderscores = grades.map(grade => grade.replace(/ /g, '_'));
    console.log('Grades with Underscores:', gradesWithUnderscores);

    // Extract grade enrollments from the selected school in the data and replace undefined values with 0
    console.log('Grades for Secondary Chart:', grades);
    console.log('Data for Secondary Chart:', data);

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
  
    
    console.log('Enrollments:', enrollments);


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

    console.log('Creating new plot with data:', bartrace, 'and layout:', layout);

    Plotly.newPlot(chartDiv, bartrace, layout);
    console.log('Chart updated successfully!');
}
