import React, { useState, useEffect, Fragment } from "react";
import { Link } from "react-router-dom";
import { Row, Col } from "react-bootstrap";
import Button from "react-bootstrap/Button";
import Card from "react-bootstrap/Card";
import axios from "axios";

function ProfileScreen(props) {
  const useAuth = localStorage.getItem("authTokenAccess");
  // const [name, setName] = useState("");
  // const [mail, setMail] = useState("");

  if (useAuth) {
    return (
      <div>
        <Card className="text-center">
          <Card.Header>Profile Details </Card.Header>
          <Card.Body>
            <Card.Title>{props.name}</Card.Title>
            <Card.Text>{props.username}</Card.Text>
          </Card.Body>
          <Card.Footer className="text-muted"></Card.Footer>
        </Card>
      </div>
    );
  }

  return (
    <Fragment>
      <h3> youre not logged in !!!! </h3>
      <p>please create an account or login</p>
      <Row className="py-3">
        <Col>
          Have an Account ? <Link to={"/login"}>Sign In</Link>
        </Col>
        <Col>
          New costomer ? <Link to={"/register"}>Sign Up</Link>
        </Col>
      </Row>
    </Fragment>
  );
}
export default ProfileScreen;
