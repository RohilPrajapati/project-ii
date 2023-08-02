// var response = JSON.parse('{{ response| tojson }}');
// data = response.iteration
// draw_chart(data)
function next_btn() {
    if (current_val + 2 >= res_data.length) {
        var btn = document.getElementById("btn_next");

        // Disable the button
        btn.disabled = true;
    }
    var btn = document.getElementById("btn_prev");

    // Disable the button
    btn.disabled = false;
    ++current_val;

    // Select the table
    var ready_msg = document.getElementById("ready_msg");
    ready_msg.style.display = "none"
    var table = document.getElementById("data_table");
    table.style.display = "table"

    // Create a new table row
    var newRow = document.createElement("tr");
    // Create cells and set their content

    // for indexing

    var i = document.createElement("td");
    i.textContent = current_val + 1;
    newRow.appendChild(i);


    // Append the cells to the row
    var count = 1
    res_tbl_head.forEach(function (head, index) {
        // Create cells and set their content
        if (index > 0) {
            var col = document.createElement("td");

            // col.textContent = "test";
            // console.log(res_data[current_val][head])
            col.textContent = res_data[current_val][head];

            // Append the cells to the row
            newRow.appendChild(col);
            count++;
        }

    });
    // for chart 
    if (val == "newtonRaphson" || val == "fixedPoint") {
        // if (val == "newtonRaphson") {
            console.log(g_data.datasets)
            console.log("working")
            if (current_val <= 0) {
                addDataset(res_data[current_val]['a'], res_data[current_val]['f(a)'], res_data[current_val]['a'], 0)
            } else {
                addDataset(res_data[current_val]['a'], res_data[current_val]['f(a)'], res_data[current_val]['a'], 0, res_data[current_val]['a'], 0, res_data[current_val - 1]['a'], res_data[current_val - 1]['f(a)'])
            }
        // }
        console.log(res_data[current_val]['a'])
        console.log(res_data[current_val]['f(a)'])
        addData(res_data[current_val]['a'], res_data[current_val]['f(a)'])
    }
    else {
        if (val == "bisection") {
            if (g_data.datasets[1]) {
                updateDataset(res_data[current_val]['a'], 0, res_data[current_val]['b'], 0)
            } else {
                addDataset(res_data[current_val]['a'], 0, res_data[current_val]['b'], 0)
            }
            if (current_val == 0) {
                addData(res_data[current_val]['a'], res_data[current_val]['f(a)'])
                addData(res_data[current_val]['b'], res_data[current_val]['f(b)'])
                addData(res_data[current_val]['c'], res_data[current_val]['f(c)'])
            }
            else {
                addData(res_data[current_val]['c'], res_data[current_val]['f(c)'])
                //if (current_val)
            }
            console.log(g_data.datasets[0]['data'])
        }

    }

    // Append the new row to the table's tbody element
    table.querySelector("tbody").appendChild(newRow);
    if (current_val + 1 == res_data.length) {
        var msg = document.getElementById("complete_msg");

        // Disable the button
        msg.style.display = "block";
    }


}
function previous_btn() {
    var table = document.getElementById('data_table');
    var ready_msg = document.getElementById("ready_msg");
    var rowCount = table.rows.length;

    // disable the btn
    if (current_val <= 0) {
        var btn = document.getElementById("btn_prev");
        btn.disabled = true;
    }
    if (rowCount > 0) {
        // graph operation in perviouse btn
        if (val == 'bisection') {

            if (current_val == 0) {
                console.log("Last")
                removeData(res_data[current_val]['a'], res_data[current_val]['f(a)'])
                removeData(res_data[current_val]['b'], res_data[current_val]['f(b)'])
                removeData(res_data[current_val]['c'], res_data[current_val]['f(c)'])
            }
            else {
                removeData(res_data[current_val]['c'], res_data[current_val]['f(c)'])
                //if (current_val)
            }
            console.log(g_data.datasets[0].data.length)

            console.log(g_data.datasets)
            
        }

        //side table operation

        table.deleteRow(rowCount - 1);
        current_val--;
        if (current_val == -1) {
            ready_msg.style.display = "block"
            table.style.display = "none"
        }

        updateDataset(res_data[current_val]['a'], 0, res_data[current_val]['b'], 0)


    }
    if ((current_val + 1) < res_data.length) {
        var msg = document.getElementById("complete_msg")
        msg.style.display = "none"
        var btn = document.getElementById("btn_next");
        // Disable the button
        btn.disabled = false;
    }
}