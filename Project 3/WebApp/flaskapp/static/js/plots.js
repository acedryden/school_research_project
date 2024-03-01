d3.json('/api/v1.0/dow_data').then(function (response) {

let trace1 = {
    x: response.names,
    y: response.high,
    text: "high",
    name: "High",
    type: "bar"
  };
  
  // Trace 2 for the Roman Data
  let trace2 = {
    x: response.names,
    y: response.low,
    text: "low",
    name: "Low",
    type: "bar"
  };
  
  // Create data array
  let data = [trace1, trace2];
  
  // Apply a title to the layout
  let layout = {
    title: "Stock High/Low in May 2023",
    barmode: "group",
    // Include margins in the layout so the x-tick labels display correctly
    margin: {
      l: 50,
      r: 50,
      b: 200,
      t: 50,
      pad: 4
    }
  };
  
  // Render the plot to the div tag with id "plot"
  Plotly.newPlot("plot", data, layout);

})
