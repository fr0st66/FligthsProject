import React, { useState, useEffect } from "react";
import axios from "axios";
import { Card } from "react-bootstrap";

const FlightsHome = () => {
  const [flights, setFlights] = useState([]);

  const getFlights = async () => {
    const result = await axios.get("http://localhost:8000/api/flight");
    setFlights(result.data);
  };

  useEffect(() => {
    getFlights();
  }, []);

  return (
    <React.Fragment>
      <div className="py-5 ">
        <div className="container">
          {flights.map((flight, i) => (
            <Card
              key={i}
              className="m-3 rounded shadow-md main-flights-show"
              style={{ width: "60em" }}
            >
              <Card.Img
                variant="top"
                src="https://www.gannett-cdn.com/presto/2019/06/23/USAT/c3a9f051-bd6c-4b39-b5b9-38244deec783-GettyImages-932651818.jpg?width=660&height=517&fit=crop&format=pjpg&auto=webp"
              />
              <Card.Body key={i}>
                <Card.Text> {flight.ID} </Card.Text>
                <Card.Title> <h1> {flight.airline} </h1> </Card.Title>
                <Card.Title> <h2> Flight to: {flight.to} </h2></Card.Title>
                <Card.Text> from: {flight.from} </Card.Text>
                <Card.Text> Flight date{flight.date} </Card.Text>

                <a  href={`/flight/${flight.ID}`}>Flight Details</a>
        
              </Card.Body>
            </Card>
          ))}
        </div>
      </div>
    </React.Fragment>
  );
};

export default FlightsHome;
