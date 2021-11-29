import 'bootstrap/dist/css/bootstrap.min.css';
import { login, test } from '../../actions/test';
import React, { useState } from "react";


export default function Login() {
  const [inputs, setInputs] = useState({
    username : "",
    password : "",
  });

  const handleChange = (event:any) => {
    const name = event.target.name;
    const value = event.target.value;
    setInputs(values => ({...values, [name]: value}))
  }

  const handleSubmit = (event:any) => {
    event.preventDefault();
    login(inputs);
    // test(inputs)
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
        <button type="submit" className="btn btn-primary">Submit</button>
      </form>

      <div>테스트 
          <button onClick={(test)}>버튼</button>
      </div>

    </>
  )
}
  
const testbutton =() => {
    // window.location.replace("/signup")
    document.location.href = "/test"
    return 
  }
    