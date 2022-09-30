import React, { useState, useEffect, Fragment } from "react";
import Row from "react-bootstrap/Row";
import axios from "axios";
import { useNavigate } from "react-router-dom";

export default function CartScreen() {
  const navigate = useNavigate();
  const cartItemsIds = JSON.parse(localStorage.getItem("cart"));
  const [items, setItems] = useState([]);
  const handleDelete = () => {
    localStorage.clear("cart");
    navigate("/cart");

  };
  

  useEffect(() => {
    if (cartItemsIds && cartItemsIds.length > 0) {
      const idsPromises = [];

      cartItemsIds.forEach(id => {
        idsPromises.push(axios.get(`http://127.0.0.1:8000/api/flight/${id}`));
      })
      
      Promise
        .all(idsPromises)
        .then(response => {
          console.log(response);
        });
    }
  });

  if (!cartItemsIds) {
    return (
      <div className="container mt-5">
        <div className="row">
          <div className="col-10 mx-auto text-center text-title text-capitalize">
            <h1>your cart is currently empty</h1>
          </div>
        </div>
      </div>
    );
  }

  return (
    <Fragment>
      <h1> My Cart </h1>
      {cartItemsIds.map((item, idx) => {
        console.log(item);
        return <Row key={idx}>Flight ID: {item}</Row>;
      })}
     <h5>  Total Flights in cart: {cartItemsIds.length} </h5>
     <button
        onClick={() => handleDelete()}
        className="btn btn-outline-primary mr-2"
      >
        Delete Flights
      </button>
    </Fragment>
  );
}
