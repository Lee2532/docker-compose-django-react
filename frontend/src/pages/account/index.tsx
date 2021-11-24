import 'bootstrap/dist/css/bootstrap.min.css';
import {Button} from "react-bootstrap";
import React, { useState } from "react";
import ReactDOM from "react-dom";


export default function Home() {
  
  return (
    <>
      <h2>home page</h2>

      <div>로그인
          <button onClick={(login)}>버튼</button>
      </div>
      
      <div>회원가입 
          <button onClick={(signup)}>버튼</button>
      </div>

      <div>차트 테스트 
          <button onClick={(charttest)}>버튼</button>
      </div>
    </>
  )
}

const login =() => {
  // window.location.replace("/login")
  document.location.href = "/login"
  return 
}

const signup =() => {
  // window.location.replace("/signup")
  document.location.href = "/signup"
  return 
}
  
const charttest =() => {
  // window.location.replace("/signup")
  document.location.href = "/charttest"
  return 
}
  