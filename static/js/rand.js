url = "/v0"

d3.json(url).then(function (response){
    let trace1 = {
        x: response.School_Number,
        y: response.Grade_8_Enrolment,
        type: 'bar'
      };
      
      let data = [trace1];
      
      let layout = {
        title: 'Test'
      };
      
    Plotly.newPlot("plot", data, layout);
      

    console.log(response)
})