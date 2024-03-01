url = '/api/v1.0/Arti/grad_data'
// d3.json(url).then(gettingDowData)
// function gettingDowData(data){
// console.log("I now can close the loop")
// console.log(data)
// }

d3.json(url).then(gettingdata);
    
function gettingdata(response){
    // let response = schooldict
    console.log(response);

    var trace1 = {
      x: response.Board_Numbers,
      y: response.Five_Year_Grads,
      mode: 'markers',
      //marker: {
          //size: [],
      //}
  };
  
  var pizza = [trace1];
  
  var show = {
      title: 'Board Names and Rates of 4yr Graduates in 2021-2022',
      showlegend: false
  };
  
  Plotly.newPlot('plot', pizza, show);
//
  let item1 = {
    x: response.Board_Numbers,
    y: response.Four_Year_Grads,
    text: "high",
    name: "High",
    type: "bar"
  };
  
  // Trace 2 for the Roman Data
  let item2 = {
    x: response.Board_Numbers,
    y: response.Four_Year_Grads_2019,
    text: "low",
    name: "Low",
    type: "bar"
  };
  
  // Create data array
  let data = [item1, item2];
  
  // Apply a title to the layout
  let layout = {
    title: "",
    // barmode: "group",
    // // Include margins in the layout so the x-tick labels display correctly
    // margin: {
    //   l: 50,
    //   r: 50,
    //   b: 200,
    //   t: 50,
    //   pad: 4
    // }
  };
  
  // Render the plot to the div tag with id "plot"
  Plotly.newPlot("plot2", data, layout);

}



  

//     var trace1 = {
//       x: [1, 2, 3, 4],
//       y: [10, 11, 12, 13],
//       mode: 'markers',
//       marker: {
//         size: [40, 60, 80, 100]
//       }
//     };
    
//     var data = [trace1];
    
//     var layout = {
//       title: 'Marker Size',
//       showlegend: false,
//       height: 600,
//       width: 600
//     };

    
// Plotly.newPlot("plot",config);

//   console.log(response)
//   };
