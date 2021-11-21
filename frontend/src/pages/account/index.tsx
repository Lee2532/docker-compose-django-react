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
      </>
    )
  }
  
  
  const signup =() => {
    window.location.replace("/signup")
    return 
  }
  
  
  const login =() => {
    window.location.replace("/login")
    return 
  }