import React from "react";
import Card from "./Components/Card";
import SX from "/Standing.jpg";
import "./Modern.css";

function Modern() {
  return (
    <>
      <div className="modern">
        <h1 className="modern-heading">Modern Poses</h1>
        <div className="modern-pose">
          <Card txt="hello" imgsrc={SX} />
          <Card txt="hello" imgsrc={SX} />
        </div>
      </div>
    </>
  );
}

export default Modern;
