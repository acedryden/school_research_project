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
        function getRate(name,year){
          for (const [key, value] of Object.entries(call)){
              if (name == key){
                for (const [key_1, value_1] of Object.entries(value)){
                  return call[name][key_1][year]
                }
              }
        }
        }
        
        layerGroup = new L.LayerGroup();

        let geolayer = L.geoJSON(response.requests[0], {
          onEachFeature: function (feature, layer) {
            hi = feature.properties.MUNICIPAL_NAME_SHORTFORM
            layer.bindPopup(`<h3>${hi}</h3><hr>
            <h4>Graduation Rate: ${getRate(hi,newData)*100}%</h4>
            `)

            layer.setStyle({color: getColor(getRate(hi,newData))}); 
             }})
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


    
