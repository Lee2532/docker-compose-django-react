import 'bootstrap/dist/css/bootstrap.min.css';
import {Button} from "react-bootstrap";
import { createuser } from '../../actions/test';
import React, { useState } from "react";
import ReactDOM from "react-dom";


export default function Signup() {
  const [inputs, setInputs] = useState({
    username : "",
    password : "",
    password2 : "",
  });

  const handleChange = (event:any) => {
    const name = event.target.name;
    const value = event.target.value;
    setInputs(values => ({...values, [name]: value}))
  }

  const handleSubmit = (event:any) => {
    event.preventDefault();
    createuser(inputs);
  }

  return (
    <>
      <h2>home page</h2>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="exampleInputUsername">Username address</label>
          <input type="text" className="form-control" name="username" value={inputs.username || ""}  onChange={handleChange} id="exampleInputUsername" aria-describedby="usernameHelp" placeholder="Enter username"/>
          <small id="usernameHelp" className="form-text text-muted">아이디를 입력해주세요.</small>
        </div>
        <div className="form-group">
          <label htmlFor="exampleInputPassword1">Password</label>
          <input type="text" className="form-control" name="password" value={inputs.password || ""} onChange={handleChange} id="exampleInputPassword1" placeholder="Password"/>
        </div>

        <div className="form-group">
          <label htmlFor="exampleInputPassword2">Password2</label>
          <input type="text" className="form-control" name="password2" value={inputs.password2 || ""} onChange={handleChange}  id="exampleInputPassword2" placeholder="Password2"/>
        </div>
        <button type="submit" className="btn btn-primary">Submit</button>
      </form>

    </>
  )
}
  
