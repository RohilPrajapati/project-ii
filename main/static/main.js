// function draw_chart(data) {
//     console.log(data[0])
//     console.table(data)
//     c = []
//     c.push(['x', 'y'])
//     for (row in data) {
//         console.log(row)
//         x_y = []
//         console.log(row)
//         console.log(row)
//         x_int = row['a'].toFixed(2);
//         y_int = row['f(a)'].toFixed(2);
//         x_y.push(parseFloat(x_int))
//         x_y.push(parseFloat(y_int))
//         c.push(x_y)
//         x_y = []
//         // x_int = data[row]['b'].toFixed(2);
//         // y_int = data[row]['f(b)'].toFixed(2);
//         // x_y.push(parseFloat(x_int))
//         // x_y.push(parseFloat(y_int))
//         // c.push(x_y)
//     }
//     r = []
//     for (row in data) {
//         x_y = []
//         // console.log(row)
//         // x_int = data[row]['a'].toFixed(2);
//         // y_int = data[row]['f(a)'].toFixed(2);
//         // x_y.push(parseFloat(x_int))
//         // x_y.push(parseFloat(y_int))
//         // c.push(x_y)
//         x_y = []
//         x_int = data[row]['b'].toFixed(2);
//         y_int = data[row]['f(b)'].toFixed(2);
//         x_y.push(parseFloat(x_int))
//         x_y.push(parseFloat(y_int))
//         r.push(x_y)
//     }
//     console.table(r)
//     r.reverse()
//     console.table(r)
//     c = c.concat(r)

//     console.table(c)

//     google.charts.load("current", { packages: ["corechart"] });
//     google.charts.setOnLoadCallback(drawChart);
//     function drawChart() {
//         var data = google.visualization.arrayToDataTable
//             (c);

//         var options = {
//             legend: 'bottom',
//             // vAxis: { minValue: -1000, maxValue: 1000 },
//             // hAxis: { minValue: -1000, maxValue: 1000 },
//             curveType: 'function',
//             pointSize: 3,
//             vAxis: {
//                 0: {}, // Default vAxis
//                 1: { position: 'right' } // Additional vAxis on the right
//             }

//         };

//         var chart = new google.visualization.LineChart(document.getElementById('chart_div'));
//         chart.draw(data, options);
//     }
// }


// function createtr(){
//     var newRow = document.createElement("tr");
//     // for (i=0;i)
//     var cell1 = document.createElement("td");
//     cell1.textContent = "row";
// }



