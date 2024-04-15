
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
  
        
        // Loop through the school array.

      for (let index = 0; index < Schools.length; index++) {  

        let school = Schools[index];
        let Color = '';
        
          // Matching the two tables

        let enrolment = enrolment_data.find(item => item.School_Number === school.School_Number)


        if (enrolment) {

          if (parseInt(enrolment.Total_Enrolment) <= 100){
            Color = "red"
          } else if (parseInt(enrolment.Total_Enrolment) <= 500){
            Color = "orange"
          } else if (parseInt(enrolment.Total_Enrolment) <= 1000){
            Color = "green"
          } else if (parseInt(enrolment.Total_Enrolment) > 1000){
            Color = "yellow"
          }
          };

          // Creating Markers for each school
          
          var colorIcon = new L.Icon({
            iconUrl: `https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-${Color}.png`,
            shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
            iconSize: [25, 41],
            iconAnchor: [12, 41],
            popupAnchor: [1, -34],
            shadowSize: [41, 41]
          }); 

                   
        let schoolMarker = L.marker([parseFloat(school.Latitude), parseFloat(school.Longitude)] ,{icon: colorIcon})
          .bindPopup("<h3>" + school.School_Name + "</h3>" + 
          "<p>Address: " + school.Street + ", " + school.City + "," + 
          "<p>Postal Code: " + school.Postal_Code + "</p>" +
          "<p>School Website: <a href='" + school.School_Website + "' target='_blank'>" + school.School_Website + "</a></p>" +
          "<p><strong>Total Enrolment:</strong> " + enrolment.Total_Enrolment + "</p>" 
          );


          // If statement to split elementary from secondary 

        if (school.School_Level === "Elementary") {
          Elementary_markerCluster.addLayer(schoolMarker);
        } else if (school.School_Level === "Secondary") {
          Secondary_markerCluster.addLayer(schoolMarker); 
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
       center: [46.9923, -81.4045],
       zoom: 6,
       layers: [streetmap, Elementary_markerCluster]
      });

      var legend = L.control({ position: "bottomright" });

      legend.onAdd = function(map) {
        var div = L.DomUtil.create("div", "legend");
        div.innerHTML += "<h4>Enrolment by School</h4>";
        div.innerHTML += '<i style="background: #FF0000"></i><span><100</span><br>';
        div.innerHTML += '<i style="background: #FFAE00"></i><span>100-500</span><br>';
        div.innerHTML += '<i style="background: #00FF00"></i><span>500-1000</span><br>';
        div.innerHTML += '<i style="background: #FFF933"></i><span>>1000</span><br>';
  
        return div;
      };
      
      legend.addTo(map);

     // Create a layer control

    L.control.layers(baseMaps, overlayMaps, {
      collapsed: false
      }).addTo(map);

    
  });
}


// API Call

d3.json("/api/v1.0/school/info.json").then(createMarkers);

