import { Container } from "react-bootstrap";
import React, { useEffect, useState } from "react";
import "./App.css";
import { Route, BrowserRouter, Routes } from "react-router-dom";
import Header from "./components/Header";
import Footer from "./components/Footer";
import Flight from "./components/Flight";
import LoginScreen from "./screens/LoginScreen";
import RegisterScreen from "./screens/RegisterScreen";
import FlightsHome from "./screens/FlightsHome";
import ProfileScreen from "./screens/ProfileScreen";
import CartScreen from "./screens/CartScreen";
import About from "./screens/About";
import axios from "axios";

function App() {
  const [name, setName] = useState("");
  const [username, setUsername] = useState("");
  const [isAdmin, setIsAdmin] = useState(false);
  const [isSuperUser, setIsSuperUser] = useState(false);
  const [flightIds, setFlightIds] = useState([]);

  // 1. get from local storage token authTokenAccess
  const userToken = localStorage.getItem("authTokenAccess");

  // 2. check if token exists
  // 3. if token => use effect to send GET request 
  useEffect(() => {
    if (userToken) {
      const LoginData = axios
        .get("http://localhost:8000/api/profile/", {
          headers: {
            Authorization: `Bearer ${userToken}`,
          },
        })
        .then((response) => {
          // 4. once response from /profile/ then => update state for consts using state hook functions
          setName(response.data.name);
          setUsername(response.data.username);
          setIsAdmin(response.data.isAdmin);
          setIsSuperUser(response.data.isSuperUser);
          console.log("STATE UPDATED!!!");
        });
    }
  });
  
  // 5. pass state consts as props to relevant components header and profile

  return (
    <div>
      <BrowserRouter>
       
        <Header name={name} isLoggedIn={!!userToken} />
        <Container>
          <main className="py-3">
            <Routes>
              <Route exact path="/" element={<FlightsHome />} />

              <Route exact path="/about" element={<About />} />

              <Route path="/login" element={<LoginScreen setUsername={setUsername} />} />

              <Route path="/register" element={<RegisterScreen />} />

              <Route path="/profile" element={<ProfileScreen name={name} username={username} />} />

              <Route path="/cart" element={<CartScreen />} />
              
              <Route path="/flight" element={<FlightsHome />} />

              <Route path="/flight/:id" element={<Flight />} />

            </Routes>
          </main>
        </Container>
      </BrowserRouter>
      <Footer />
    </div>
  );
}

export default App;
