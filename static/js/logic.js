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
  return go
  }


url_mongo = "/mongo"
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

        L.geoJSON(response.requests[0], {
          onEachFeature: function (feature, layer) {
            hi = feature.properties.MUNICIPAL_NAME_SHORTFORM
            layer.bindPopup(`<h3>${hi}</h3><hr>
            <h4>Graduation Rate 2017-2018: ${getRate(hi,"Five_2017_2018")}</h4>
            <h4>Graduation Rate 2017-2018: ${getRate(hi,"Four_2017_2018")}</h4>
            <h4>Graduation Rate 2017-2018: ${getRate(hi,"Four_2018_2019")}</h4>
            `)

            layer.setStyle({color: getColor(getRate(hi,"Five_2017_2018"))}); 
             }}).addTo(myMap)
      
      })
















      
    })




    