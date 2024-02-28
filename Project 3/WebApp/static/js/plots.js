url = '/api/v1.0/dow_data'
// d3.json(url).then(gettingDowData)
// function gettingDowData(data){
// console.log("I now can close the loop")
// console.log(data)
// }

d3.json(url).then(gettingDowData)

function gettingDowData(data) {
console.log(data)

let id = data (splice(1,0))
let schoolname = data (splice (0,1))
  
    let trace1 = {
        x: id, 
        y: schoolname, 
        type:"bar"
    }

    let item = [trace1]

    let layout = {
        title: "Names of Schools in Ontario",
    }

    Plotly.newPlot('plot', item, layout)
}