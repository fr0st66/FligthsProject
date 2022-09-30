import React, { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { Row, Col, Button, Form } from "react-bootstrap";
import axios from "axios";

const RegisterScreen = (location, history) => {
  const navigate = useNavigate();
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");

  const submitHandler = async (e) => {
    e.preventDefault();

    const registerResponse = await axios.post('http://localhost:8000/api/register/', {
      name: name,
      email: email,
      password: password
     });

     setName("");
     setEmail("");
     setPassword("");

    navigate("/login");
  }
  
  return (
    <div>
      <h3>Register</h3>

      <Form onSubmit={submitHandler}>

        <Form.Group controlId="name" >
          <Form.Label>Name</Form.Label>
          <Form.Control
            required
            type="name"
            placeholder="Enter Name"
            value={name}
            onChange={(e) => setName(e.target.value)}
          />
        </Form.Group>

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

        <Form.Group controlId="passwordConfirm">
          <Form.Label>Confirm Password</Form.Label>
          <Form.Control
            required
            type="password"
            placeholder="Confirm Password"
            value={confirmPassword}
            onChange={(e) => setConfirmPassword(e.target.value)}
          />
        </Form.Group>

        <Button type="submit" variant="primary" className="mt-3">
          Register
        </Button>
        
      </Form>
      <Row className="py-3">
        <Col>
          Have an Account ?{" "}
           <Link to={"/login"}>
           Sign In
          </Link>
         </Col>
      </Row>
    </div>
  );


}
export default RegisterScreen;