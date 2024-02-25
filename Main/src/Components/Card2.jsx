import React from "react";
import Car from "/Car1.jpeg";
import "./Card2.css";

function Card2(props) {
  return (
    <div class="card">
      <div class="imgbox">
        <img src={Car} />
      </div>
      <div class="content">
        <h3>post title</h3>
        <p>
          lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do
          eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad
          minim veniam, quis nostrud exercitation ullamcon Ut enim ad minim
          veniam, quis nostrud exercitation
        </p>
      </div>
    </div>
  );
}

export default Card2;
