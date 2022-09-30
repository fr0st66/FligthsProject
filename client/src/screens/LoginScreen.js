import React, { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { Row, Col, Button, Form } from "react-bootstrap";
import axios from "axios";


const LoginScreen = (props) => {
  const navigate = useNavigate();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

// login handler
  const submitHandler = async (event) => {
    event.preventDefault();

    const loginResponse = await axios.post("http://localhost:8000/api/login/", {
      username: email,
      password: password,
     
    }); 
    //reset form fields
    setEmail("");
    setPassword("");

    localStorage.setItem("authTokenAccess", loginResponse.data.access);
    // localStorage.setItem("authTokenRefresh", loginResponse.data.refresh);

    props.setUsername("");
    navigate("/");

    };

  return (
    <div>
      <h3>Login</h3>

      <Form onSubmit={submitHandler}>
        <Form.Group controlId="email">
          <Form.Label>Email Address</Form.Label>
          <Form.Control
            required
            type="email"
            placeholder="Enter Email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
        </Form.Group>

        <Form.Group controlId="password">
          <Form.Label>Password</Form.Label>
          <Form.Control
            required
            type="password"
            placeholder="Enter Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
        </Form.Group>

        <Button type="submit" variant="primary" className="mt-3">
          login
        </Button>
      </Form>
      <Row className="py-3">
        <Col>
          New costomer ? <Link to={"/register"}> Register</Link>
        </Col>
      </Row>
    </div>
  );
  
};

export default LoginScreen;
