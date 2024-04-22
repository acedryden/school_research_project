// Initialize map
let map = L.map("map-id", {
  center: [46.9923, -81.4045],
  zoom: 6
});

// Create Tile Layer
let streetmap = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
});

// Create a baseMaps 
let baseMaps = {
  "Street Map": streetmap
};

// Create empty overlayMaps
let Elementary_markerCluster = L.markerClusterGroup();
let Secondary_markerCluster = L.markerClusterGroup();
let overlayMaps = {
  "Elementary School": Elementary_markerCluster,
  "Secondary School": Secondary_markerCluster
};

// Add streetmap to the map
streetmap.addTo(map);

// Create a layer control
let layerControl = L.control.layers(baseMaps, overlayMaps, {
  collapsed: false
}).addTo(map);

// Add legend
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

// Function to create markers
function createMarkers(response, selectedYear) {
  // Assign schools to a variable
  let Schools = response;

  // Importing the Enrolment data
  d3.json(`/api/v1.0/predicted/${selectedYear}.json`)
    .then(function(enrolment_data_response) {

      let enrolment_data = enrolment_data_response;
      
      // Clear existing markers in clusters
      Elementary_markerCluster.clearLayers();
      Secondary_markerCluster.clearLayers();

      // Loop through the school array.
      for (let index = 0; index < Schools.length; index++) {
        let school = Schools[index];
        let Color = '';

        // Matching the two tables
        let enrolment = enrolment_data.find(item => item.School_Number === school.School_Number);

        if (enrolment && enrolment.Total_Enrolment !== undefined) {
          if (parseInt(enrolment.Total_Enrolment) <= 100) {
            Color = "red";
          } else if (parseInt(enrolment.Total_Enrolment) <= 500) {
            Color = "orange";
          } else if (parseInt(enrolment.Total_Enrolment) <= 1000) {
            Color = "green";
          } else if (parseInt(enrolment.Total_Enrolment) > 1000) {
            Color = "yellow";
          }
        }

        // Creating Markers for each school if enrolment data is available
        if (enrolment && enrolment.Total_Enrolment !== undefined) {
          var colorIcon = new L.Icon({
            iconUrl: `https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-${Color}.png`,
            shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
            iconSize: [25, 41],
            iconAnchor: [12, 41],
            popupAnchor: [1, -34],
            shadowSize: [41, 41]
          });

        // Create school marker
        let schoolMarker = L.marker([parseFloat(school.Latitude), parseFloat(school.Longitude)], { icon: colorIcon })
          .bindPopup("<h3>" + school.School_Name + "</h3>" +
            "<p>Address: " + school.Street + ", " + school.City + "," +
            "<p>Postal Code: " + school.Postal_Code + "</p>" +
            "<p>School Website: <a href='" + school.School_Website + "' target='_blank'>" + school.School_Website + "</a></p>"  +
            "<p><strong>Total Enrolment:</strong> " + enrolment.Total_Enrolment + "</p>"
          );

        // If statement to split elementary from secondary
        if (school.School_Level === "Elementary") {
          Elementary_markerCluster.addLayer(schoolMarker);
        } else if (school.School_Level === "Secondary") {
          Secondary_markerCluster.addLayer(schoolMarker);
        }
      }
    }
  })
    .catch(function(error) {
      console.log("Error fetching enrolment data:", error);
    });
}

// Create dropdown menu control for selecting year
var yearControl = L.Control.extend({
  onAdd: function(map) {
    var dropdownContainer = L.DomUtil.create('div', 'year-control');
    dropdownContainer.innerHTML = `
      <select id="year-dropdown">
        <option value="2022">2019</option>
        <option value="2022">2020</option>
        <option value="2021">2021</option>
        <option value="2022">2022</option>
        <option value="2023">2023</option>
        <option value="2024">2024</option>
        <option value="2025">2025</option>
        <option value="2026">2026</option>
      </select>
    `;
    L.DomEvent.disableClickPropagation(dropdownContainer);
    return dropdownContainer;
  }
});

// Add dropdown menu control to the map
(new yearControl()).addTo(map);

// Event listener for year dropdown change
document.getElementById("year-dropdown").addEventListener("change", function() {
  let selectedYear = this.value;
  // Reload data for the selected year
  d3.json("/api/v1.0/school/info.json")
    .then(function(response) {
      createMarkers(response, selectedYear);
    })
    .catch(function(error) {
      console.log("Error fetching school info:", error);
    });
});

// Initial call to createMarkers with default year
let defaultYear = 2019; 
d3.json("/api/v1.0/school/info.json")
  .then(function(response) {
    createMarkers(response, defaultYear);
  })
  .catch(function(error) {
    console.log("Error fetching school info:", error);
  });


