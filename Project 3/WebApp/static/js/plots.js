url = '/api/v1.0/dow_data'
// d3.json(url).then(gettingDowData)
// function gettingDowData(data){
// console.log("I now can close the loop")
// console.log(data)
// }

d3.json(url).then(makeGraph)

function makeGraph(response) {
    may_high = response.high
    may_low = response.low
    stock_names = response.names

    let trace1 = {
        x: stock_names, 
        y: may_high, 
        text: 'high',
        name: "High",
        type: 'bar'
    }

    let trace2 = {
        x: stock_names, 
        y: may_low, 
        text: 'low', 
        name: 'Low', 
        type: 'bar'
    }

    let data = [trace1, trace2]

    let layout = {
        title: "Stock High/Low in May 2023",
        barmode: "group",
        margin: {
          l: 50,
          r: 50,
          b: 200,
          t: 50,
          pad: 4
        }
    }

    Plotly.newPlot('plot', data, layout)
}