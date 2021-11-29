import CSVReader from "react-csv-reader";
import { render } from "@testing-library/react";


export default function ReadCsv() {
  // const handleForce = (data:any, fileInfo:any) => console.log(data, fileInfo);
  const handleForce = (data:any) => console.log(data);

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
    </div>
  );

  return(
    <>
    {reader}
    
    <div>테스트</div>
    </>
    
  )
// ReactDOM.render(reader, document.getElementById("root"));
}