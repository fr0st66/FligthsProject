import axios from "axios";
import React, { useState, useEffect } from "react";
import { useParams } from "react-router";
import { useNavigate } from "react-router-dom";
import { Card } from "react-bootstrap";

const Flight = (props) => {
  const navigate = useNavigate();
  const [flight, setFlight] = useState([]);
  const { id } = useParams();

  const getSingleFlight = async () => {
    const { data } = await axios.get(`http://127.0.0.1:8000/api/flight/${id}`);
    setFlight(data);
  };

  useEffect(() => {
    getSingleFlight();
  }, []);
  // add to cart-pass flight id
  const addFlightToCart = (flightId) => {
    // check if wh have some flights in local storage
    const currentCart = localStorage.getItem("cart");

    if (currentCart) {
      // if we have- then add them
      const cartIds = JSON.parse(currentCart);
      const newCartIds = [...cartIds, flightId];
      // save them to local storage (new and old)
      localStorage.setItem("cart", JSON.stringify(newCartIds));
    } else {
      localStorage.setItem("cart", JSON.stringify([flightId]));
    }
    console.log(JSON.parse(currentCart));
    navigate("/cart");
  };

  return (
    <div>
      <Card
        className="m-3 rounded shadow-md main-flights-show"
        style={{ width: "60em" }}
      >
        <Card.Img
          variant="top"
          src="https://th.bing.com/th/id/OIP.zXOKJWF4OHBLbc7Y4a5bUwHaEK?pid=ImgDet&rs=1"
        />
        <Card.Body>
          <Card.Text> {flight.ID} </Card.Text>
          <Card.Title>
            {" "}
            <h1> {flight.airline} </h1>{" "}
          </Card.Title>
          <Card.Title>
            {" "}
            <h2> Flight to: {flight.to} </h2>
          </Card.Title>
          <Card.Text> from: {flight.from} </Card.Text>
          <Card.Text> Flight date{flight.date} </Card.Text>
          <button
            onClick={() => addFlightToCart(id)}
            className="btn btn-outline-primary mr-2"
          >
            Add to Cart
          </button>
        </Card.Body>
      </Card>
    </div>
  );
};

export default Flight;
