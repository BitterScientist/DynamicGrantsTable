function createDropDown() {
    var selector = d3.select("#selDataset");
    d3.json("/categories").then((sampleNames) => {
        sampleNames.forEach((sample) => {
          console.log(sample);
          selector
            .append("option")
            .text(sample)
            .property("value", sample);
        });
    });
  }
  
  
  function initializeTable() {
    d3.json("/categories").then(function (data) {
      console.log(data)
      var category = data[0];
      console.log(category);
      contructTable(category);
    });
  }
  
  function contructTable(species) {
    d3.json(`/filtered_awards/${species}`).then(function (data) {
      var tableData = data;
  
      // Select the table header tag
      var thead = d3.select('thead');
      thead.html("");

      // Append info for each warning to the table body
      const header_keys = Object.keys(data[0]);
      console.log(header_keys)
      Object.entries(header_keys).forEach(function([key, value]) {
        //Append all values of the event to the row
        var th = thead.append("th").text(value);
      });

      // Select the table body tag
      var tbody = d3.select("tbody");
      tbody.html("");
  
      tableData.forEach(event => {
        //Create new row for each warning
        var row = tbody.append("tr");
        Object.entries(event).forEach(function([key, value]) {
            if (key == "6. Link") {
              var td = row.append("td")
              .append("a")
              .attr("xlink:href", value)
              .html("Link")
              .style("cursor", "pointer")
              .on("click", function(d) { window.open(value, "_blank"); });
            } else {
            var td = row.append("td").text(value);
            }
        });
    });
  });
  }
  
  function updateTable(species) {
    d3.json(`/filtered_awards/${species}`).then(function (data) {
  
      var tableData = data;

      // Select the table header tag
      var thead = d3.select('thead');
      thead.html("");

      // Append info for each warning to the table body
      const header_keys = Object.keys(data[0]);
      console.log(header_keys)
      Object.entries(header_keys).forEach(function([key, value]) {
        //Append all values of the event to the row
        var th = thead.append("th").text(value);
      });

      // Select the table body tag
      var tbody = d3.select("tbody");
      tbody.html("");
  
      tableData.forEach(event => {
        //Create new row for each warning
        var row = tbody.append("tr");
        Object.entries(event).forEach(function([key, value]) {
            if (key == "6. Link") {
              var td = row.append("td")
              .append("a")
              .attr("xlink:href", value)
              .html("Link")
              .style("cursor", "pointer")
              .on("click", function(d) { window.open(value, "_blank"); });
            } else {
            var td = row.append("td").text(value);
            }
        });
    });
    });
  }
  
  function init() {
    createDropDown();
    initializeTable();
  }

  // Fetch new data each time a new sample is selected
  function onClick() {
    d3.json(`/all_awards`).then(function(data) {
      var tableData = data;
  
      // Select the table header tag
      var thead = d3.select('thead');
      thead.html("");

      // Append info for each warning to the table body
      const header_keys = Object.keys(data[0]);
      console.log(header_keys)
      Object.entries(header_keys).forEach(function([key, value]) {
        //Append all values of the event to the row
        var th = thead.append("th").text(value);
      });

      // Select the table body tag
      var tbody = d3.select("tbody");
      tbody.html("");
  
      // Append to the table body
      tableData.forEach(event => {
          //Create new row for each warning
          var row = tbody.append("tr");
          Object.entries(event).forEach(function([key, value]) {
              if (key == "6. Link") {
                var td = row.append("td")
                .append("a")
                .attr("xlink:href", value)
                .html("Link")
                .style("cursor", "pointer")
                .on("click", function(d) { window.open(value, "_blank"); });
              } else {
              var td = row.append("td").text(value);
              }
          });
      });
    });
  }

  
    // Fetch new data each time a new sample is selected
  function optionChanged(newSelection) {
    console.log(newSelection);
    updateTable(newSelection);
  }
  
  init();
  