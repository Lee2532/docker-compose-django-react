import React from "react";
import {
  BrowserRouter,
  Routes,
  Route,
  useRoutes,
} from "react-router-dom";

import Home from "./pages/account/index";
import Signup from "./pages/account/signup";
import Error from "./common/Error"
import 'bootstrap/dist/css/bootstrap.min.css';

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />}></Route>
        <Route path="/signup" element={<Signup />}></Route>
        <Route path="*" element={<Error />}></Route>
      </Routes>
    </BrowserRouter>

  );
}

