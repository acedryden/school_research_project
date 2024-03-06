// Creating the map object

let street = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  })

function getColor(grad_rate){
  if (grad_rate < 0.6){
    return "yellow"
  }
  else if (grad_rate < 0.7){
    return "orange"
  }
  else if (grad_rate < 0.8){
    return "red"
  }
  else if (grad_rate < 0.9){
    return "blue"
  }
  else if (grad_rate < 1){
    return "green"
  }
}


let myMap = L.map("map", {
    center: [43.6532, -79.3832],
    zoom: 17,
    layers: street
  });

function optionChanged(go){
  myMap.removeLayer(layerGroup);
  boundaries(go)
  }

function boundaries(newData){
  url_mongo = "/api/v0/boundaries.json"
    d3.json(url_mongo).then(function (response){
      url_mongo = "/api/v0/grad_rate"
      d3.json(url_mongo).then(function (call){
        function getRate(board_name,year){
         return call[board_name][year]   
        }
        layerGroup = new L.LayerGroup();

        let geolayer = L.geoJSON(response.requests[0], {
          onEachFeature: function (feature, layer){ 
            layer.setStyle({color: getColor(getRate(feature.properties.BOARD_NUM,newData))}); 
            
            
            layer.bindPopup(`<h3>${feature.properties.BOARD_NAME
            }</h3><hr>
            <h4>Graduation Rate: ${(getRate(feature.properties.BOARD_NUM,newData)*100).toFixed(2)}%</h4>
            `)

             }}).addTo(myMap)
         layerGroup.addTo(myMap);
         layerGroup.addLayer(geolayer);
      })

    })

}

boundaries("Four_2017_2018")

var legend = L.control({position: "bottomright"});
legend.onAdd = function (map) {
  
  var div = L.DomUtil.create('div', 'info legend'),
      grades = [50, 60, 70, 80, 90]
      

  // loop through our density intervals and generate a label with a colored square for each interval
  for (var i = 0; i < grades.length; i++) {
      div.innerHTML +=
          '<i style="background:' + getColor((grades[i] + 1)/100) + '"></i> ' +
          grades[i] + (grades[i + 1] ? '&ndash;' + grades[i + 1] + '<br>' : '+');
  }

  return div;
};

legend.addTo(myMap);

    