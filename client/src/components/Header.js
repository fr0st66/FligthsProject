import Container from "react-bootstrap/Container";
import Nav from "react-bootstrap/Nav";
import Navbar from "react-bootstrap/Navbar";
import React from "react";
import { useNavigate } from "react-router-dom";


function Header(props) {
  // for navigate after get token
  const navigate = useNavigate();
// logout handle - delete token from local storage
  const handleLogout = () => {
    localStorage.clear("authTokenAccess");
    navigate("/");
  };
// props- from App 
  if (props.isLoggedIn)
   {
    return (
      <Navbar collapseOnSelect expand="lg" bg="dark" variant="dark">
        <Container>
          <Navbar.Brand href="/">Nancys Travel</Navbar.Brand>
          <Navbar.Toggle aria-controls="responsive-navbar-nav" />
          <Navbar.Collapse id="responsive-navbar-nav">
            <Nav className="me-auto">
              <Nav.Link href="/about">About </Nav.Link>
            </Nav>
            <Nav>
              <Navbar.Text>
                <a href="/profile"> Signed in as: {props.name}</a>
              </Navbar.Text>
              <Nav.Link href="/cart">Cart</Nav.Link>
              <Nav.Link href="/profile">Rrofile</Nav.Link>
              <Nav.Link onClick={handleLogout}>Logout</Nav.Link>
            </Nav>
          </Navbar.Collapse>
        </Container>
      </Navbar>
    );
  }
//  if token not exist in local storage
  return (
    <Navbar collapseOnSelect expand="lg" bg="dark" variant="dark">
      <Container>
        <Navbar.Brand href="/">Nancys Travel</Navbar.Brand>
        <Navbar.Toggle aria-controls="responsive-navbar-nav" />
        <Navbar.Collapse id="responsive-navbar-nav">
          <Nav className="me-auto">
            <Nav.Link href="/">About </Nav.Link>
          </Nav>
          <Nav>
          <Navbar.Text>
                <a href="/login"> NOT log in  </a>
              </Navbar.Text>
            <Nav.Link href="/cart">Cart</Nav.Link>
            <Nav.Link href="/register">Register</Nav.Link>
            <Nav.Link eventKey={2} href="/login">
              Login
            </Nav.Link>
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
}

export default Header;
