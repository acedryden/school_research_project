url = '/api/v1.0/Arti/grad_data'

//Bubble/Scatter Plot
d3.json(url).then(gettingdata);
    
function gettingdata(response){
    // let response = schooldict
    console.log(response);

    var trace1 = {
      x: response.Board_Numbers,
      y: response.Four_Year_Grads,
      text: response.Board_Names,
      
      mode: 'markers',
      marker: {
        size: 10,
        color: "green", 
        opacity: [0.4]
       }
  };
  var trace2 = {
    x: response.Board_Numbers,
    y: response.Four_Year_Grads_2019,
    text: response.Board_Names,
    
    mode: 'markers',
    marker: {
      size: 10,
      color: "blue", 
      opacity: [0.8]
     }
  };

  var trace3 = {
    x: response.Board_Numbers,
    y: response.Five_Year_Grads,
    text: response.Board_Names,
    
    mode: 'markers',
    marker: {
      size: 10 ,
      color: "orange",
      opacity:[0.6] 
     }
  };
  
  var pizza = [trace1,trace2,trace3];
  
  var show = {
      title: 'Rates of Graduation By Board 2021-2022',
      showlegend: false
  };
  
  Plotly.newPlot('plot', pizza, show);

//Line Chart
  // let item1 = {
  //   x: response.Board_Numbers,
  //   y: response.Four_Year_Grads,
  //   text: "%",
  //   name: "Four Year Graduation Rate 2017-2018 Grade 9 Cohort",
  //   type: "line"
  // };
  
  // // Trace 2 for the 2018-2019 cohort
  // let item2 = {
  //   x: response.Board_Numbers,
  //   y: response.Four_Year_Grads_2019,
  //   text: "%",
  //   name: "Four Year Graduation Rate 2018-2019 Grade 9 Cohort",
  //   type: "line"
  // };

  // //
  // let item3 = {
  //   x: response.Board_Numbers,
  //   y: response.Five_Year_Grads,
  //   text: "%",
  //   name: "Five Year Graduation Rate 2017-2018 Grade 9 Cohort",
  //   type: "line"
  // };
  
  // // Create data array
  // let data = [item1, item2, item3];
  
  // // Apply a title to the layout
  // let layout = {
  //   title: "Graduation Rates Across Ontario 2021-2022", 
  //   };
  
  // // Render the plot to the div tag with id "plot"
  // Plotly.newPlot("plot2", data, layout);

  //Bar Chart
  let info1 = {
    x: response.Regions,
    y: response.Four_Year_Grads,
    text: "%",
    name: "Four Year Graduation Rate 2017-2018 Grade 9 Cohort",
    type: "bar"
  };
  
  // Trace 2 for the 2018-2019 cohort
  let info2 = {
    x: response.Regions,
    y: response.Four_Year_Grads_2019,
    text: "%",
    name: "Four Year Graduation Rate 2018-2019 Grade 9 Cohort",
    type: "bar"
  };

  //
  let info3 = {
    x: response.Regions,
    y: response.Five_Year_Grads,
    text: "%",
    name: "Five Year Graduation Rate 2017-2018 Grade 9 Cohort",
    type: "bar"
  };
  
  // Create data array
  let read = [info1, info2, info3];
  
  // Apply a title to the layout
  let panel = {
    title: "Graduation Rates Across Ontario By Region", 
  };
  
  // Render the plot to the div tag with id "plot"
  Plotly.newPlot("plot3", read, panel);

}
