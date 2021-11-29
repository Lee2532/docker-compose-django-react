import {
  BrowserRouter,
  Routes,
  Route,
} from "react-router-dom";

import Home from "./pages/account/index";
import Signup from "./pages/account/signup";
import Login from "./pages/account/login";
import ReadCsv from "./pages/chart/chattest";
import Error from "./common/Error"
import 'bootstrap/dist/css/bootstrap.min.css';

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />}></Route>
        <Route path="/signup" element={<Signup />}></Route>
        <Route path="/login" element={<Login />}></Route>
        {/* <Route path="/test" element={<Test />}></Route> */}
        <Route path="/readcsv" element={<ReadCsv />}></Route>
        <Route path="*" element={<Error />}></Route>
      </Routes>
    </BrowserRouter>

  );
}

