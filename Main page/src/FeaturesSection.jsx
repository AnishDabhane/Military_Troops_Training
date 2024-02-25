import React from "react";
import "./FeaturesSection.css";
import Card2 from "./Components/Card2";

const FeaturesSection = () => {
  return (
    <>
      <div className="headin">Salient Features</div>
      <div className="featur">
        <Card2 />
        <Card2 />
        <Card2 />
      </div>
    </>
  );
};

export default FeaturesSection;
