// Get data
d3.csv("https://raw.githubusercontent.com/fionaliu0621/LATIA112-1/main/4f151e9b-6f41-441f-9060-fe00940ba54f.csv").then(
    res => {
        console.log(res);
        drawLineChart(res);
    }
);

function drawLineChart(res) {
    let myGraph = document.getElementById("myGraph");
    let myGraph2 = document.getElementById('myGraph2');
    let myGraph3 = document.getElementById('myGraph3');

    // Draw Line Chart
    let trace1 = {
        mode: "lines+markers",
        type: "scatter",
        name: "訓練次數",
        marker: {
            size: 10
        },
        x: [],
        y: [],
        text: [],
        textposition: "bottom center",
        textfont: {
            family: "Raleway, sans-serif",
            size: 15,
            color: "blue"
        }
    };

    for (let i = 0; i < res.length; i++) {
        trace1.x[i] = res[i]["課程類別"];
        trace1.y[i] = res[i]["次數"];
        trace1.text[i] = res[i]["title"];
    }

    let data = [trace1];
    let layout = {
        margin: {
            t: 80
        },
        title: "訓練次數折線圖"
    };

    Plotly.newPlot(myGraph, data, layout);

    // Draw Bar Chart
    let trace2 = {
        type: 'bar',
        name: '訓練時數',
        x: [],
        y: [],
        text: [],
        textposition: "bottom center",
        textfont: {
            family: "Raleway, sans-serif",
            size: 15,
            color: "blue"
        }
    };

    for (let i = 0; i < res.length; i++) {
        trace2.x[i] = res[i]['課程類別'];
        trace2.y[i] = res[i]['時數'];
        trace2.text[i] = res[i]["title"];
    }

    let data2 = [trace2];
    let layout2 = {
        margin: {
            t: 0
        },
        title: "訓練時數長條圖"
    };

    Plotly.newPlot(myGraph2, data2, layout2);

    // Draw Pie Chart
    let aggregatedData = {};
    for (let i = 0; i < res.length; i++) {
        let category = res[i]['課程類別'];
        let count = parseInt(res[i]['人次']);

        // Extract common prefix, e.g., "政策能力訓練"
        let commonPrefix = category.match(/^(.+?)\(/)?.[1] || category;

        if (aggregatedData[commonPrefix]) {
            aggregatedData[commonPrefix] += count;
        } else {
            aggregatedData[commonPrefix] = count;
        }
    }

    // Create data for the pie chart
    let trace3 = {
        type: 'pie',
        labels: Object.keys(aggregatedData),
        values: Object.values(aggregatedData),
        text: Object.keys(aggregatedData).map(category => `${category}<br>${aggregatedData[category]} 人`),
        hoverinfo: 'label+percent',
    };

    let data3 = [trace3];
    let layout3 = {
        margin: {
            t: 0
        },
        title: "課程類別人數比例"
    };

    Plotly.newPlot(myGraph3, data3, layout3);
}
