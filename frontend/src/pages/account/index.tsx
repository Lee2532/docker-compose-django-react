import 'bootstrap/dist/css/bootstrap.min.css';
import {Button} from "react-bootstrap";

export default function Home() {
    return (
      <>
        <h2>home page</h2>
        <Button>Boot strap</Button>
        <div>로그인
            <button onClick={(login)}>버튼</button>
        </div>
        
        <div>회원가입 
            <button onClick={(signup)}>버튼</button>
        </div>
      </>
    )
  }
  
  const login =() => {
    window.location.replace("/login")
    return 
  }
  
  const signup =() => {
    window.location.replace("/signup")
    return 
  }
  
  