import 'bootstrap/dist/css/bootstrap.min.css';
import {Button} from "react-bootstrap";
import React, { useState } from "react";
import ReactDOM from "react-dom";
import { BootstrapTable, TableHeaderColumn } from 'react-bootstrap-table';


export default function ChartTest() {
  

  return (
    <>
      <h1>테이블</h1>


      <table className="table-striped border-success">
        <thead>
          <tr>
            <th data-field="id">
              <span className="text-success">
                Employee ID
              </span>
            </th>
            <th data-field="name">
              <span className="text-success">
                Employee Name 
              </span>
            </th>
            <th data-field="date">
              <span className="text-success">
                Joining Date 
              </span>
            </th>
          </tr>
        </thead>
      </table>

    </>
  )
}
