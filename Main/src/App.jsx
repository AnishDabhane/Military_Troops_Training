import { useState } from "react";
import Navbar from "./Navbar";
import viteLogo from "/vite.svg";
import "./App.css";
import Hero from "./Hero";
import PoseOverview from "./PoseOverview";
import Modern from "./Modern";
import FeaturesSection from "./FeaturesSection";

function App() {
  return (
    <>
      <Navbar />
      <Hero />
      <FeaturesSection />
      <PoseOverview />
      <Modern />
    </>
  );
}

export default App;
