
function createMarkers(response) {
      
      // Asigh schools to a variable
    
    let Schools = response;


      // Importing the Enrolment data

    let Enrolment_Data = d3.json("/api/v1.0/enrollment.json");

    // Enrolment API Call

    Enrolment_Data.then(function(enrolment_data_response){

        // Asigning Enrolment Dataset to a variable

      let enrolment_data = enrolment_data_response
  
        // Initialize an array to hold School Markers.

      let Elementary_markerCluster = L.markerClusterGroup();
      let Secondary_markerCluster = L.markerClusterGroup();
  
        // Assigning Markers Color to Variables

      let Color = ""

        // Loop through the stations array.

      for (let index = 0; index < 500; index++) {  //Schools.length

        let school = Schools[index];

        
          // Matching the two tables

        let enrolment = enrolment_data.find(item => item.School_Number === school.School_Number)


        if (enrolment) {

          if (enrolment.Total_Enrolment <= 300){
            Color = "red"
          } else if (enrolment.Total_Enrolment <= 500){
            Color = "orange"
          } else if (enrolment.Total_Enrolment <= 1000){
            Color = "green"
          } else if (enrolment.Total_Enrolment > 1000){
            Color = "yellow"
          }

        let CustomMarker = L.ExtraMarkers.icon({

          icon: 'fa-coffee',
          markerColor : Color,
          shape: 'circle',
          prefix: 'fa'
    
        });

          // Creating Markers for each school

        let schoolMarker = L.marker([parseFloat(school.Latitude), parseFloat(school.Longitude),{icon: CustomMarker}])
          .bindPopup("<h3>" + school.School_Name + "</h3>" + 
          "<p>Address: " + school.Street + ", " + school.City + "," + 
          "<p>Postal Code: " + school.Postal_Code + "</p>");


          // If statement to split elementary from secondary 

        if (school.School_Level === "Elementary") {
          Elementary_markerCluster.addLayer(schoolMarker);
        } else if (school.School_Level === "Secondary") {
          Secondary_markerCluster.addLayer(schoolMarker); 
        }
      }

      }

      // Create Tile Layer

    let streetmap = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
      });


     // Create a baseMaps 

    let baseMaps = {
      "Street Map": streetmap
      };

     // Create an overlayMaps

    let overlayMaps = {
      "Elementary Location": Elementary_markerCluster,
      "Secondary School" : Secondary_markerCluster
      };

      // Create the map 

    let map = L.map("map-id", {
       center: [45.1623, -81.4045],
       zoom: 6,
       layers: [streetmap, Elementary_markerCluster]
      });

     // Create a layer control

    L.control.layers(baseMaps, overlayMaps, {
      collapsed: false
      }).addTo(map);


  });
}

// API Call

d3.json("/api/v1.0/school/info.json").then(createMarkers);