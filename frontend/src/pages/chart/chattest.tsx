import React from "react";
import ReactDOM from "react-dom";
import CSVReader from "react-csv-reader";


export default function Test2() {
  const handleForce = (data:any, fileInfo:any) => console.log(data, fileInfo);

  const papaparseOptions = {
    header: true,
    dynamicTyping: true,
    skipEmptyLines: true,
    transformHeader: (header:any) => header.toLowerCase().replace(/\W/g, "_")
  };

  const reader = (
    <div className="container">
      <CSVReader
        cssClass="react-csv-input"
        label="Select CSV with secret Death Star statistics"
        onFileLoaded={handleForce}
        parserOptions={papaparseOptions}
      />
      <p>and then open the console</p>
      <div>{handleForce}</div>
    </div>
  );
    return(
      <>
      {reader}
      </>
      
    )
// ReactDOM.render(reader, document.getElementById("root"));
}