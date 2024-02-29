// Creating the map object
url = "/idk"

d3.json(url).then(function (response){
  let markers = L.markerClusterGroup();
    for (let i = 0; i < response.Longitude.length; i++) {
      //console.log(response.Longitude[i])
      markers.addLayer(L.marker([response.Latitude[i], response.Longitude[i]]));
        
    }
    myMap.addLayer(markers);
})

let street = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  })

toronto = L.geoJson(point)
ontario = L.geoJson(bounds)

let baseMaps = {
  "Street Map": street
};


let overlayMaps = {
  "Toronto": toronto,
  "Ontario": ontario
};

let myMap = L.map("map", {
    center: [43.6532, -79.3832],
    zoom: 17,
    layers: [street, toronto, ontario]
  });
  
  // Adding the tile layer
  
  
  // Use this link to get the GeoJSON data.
  function onEachFeature(feature, layer) {
    // does this feature have a property named popupContent?
    if (feature.properties) {
        layer.bindPopup(feature.properties);
    }
}
  // Getting our GeoJSON data

    L.control.layers(baseMaps, overlayMaps, {
      collapsed: false
    }).addTo(myMap);




