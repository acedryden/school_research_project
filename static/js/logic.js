// Creating the map object
let myMap = L.map("map", {
    center: [43.6532, -79.3832],
    zoom: 17
  });
  
  // Adding the tile layer
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  }).addTo(myMap);
  
  // Use this link to get the GeoJSON data.
  function onEachFeature(feature, layer) {
    // does this feature have a property named popupContent?
    if (feature.properties) {
        layer.bindPopup(feature.properties);
    }
}
  // Getting our GeoJSON data
  
  L.geoJson(school).addTo(myMap);
  
    // Creating a GeoJSON layer with the retrieved data
  L.geoJson(point).addTo(myMap);
  
  
  L.geoJSON(school, {
    onEachFeature: onEachFeature
}).addTo(myMap);

  

