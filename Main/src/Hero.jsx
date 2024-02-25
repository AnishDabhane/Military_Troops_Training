import React from "react";
import "./Hero.css";
import ImgReveal from "./Components/ImgReveal";
import { animate, motion } from "framer-motion";

function Hero() {
  return (
    <>
      <div className="herox">
        <ImgReveal />
        <div className="hero-line-container">
          <motion.div
            className="hero-line"
            initial={{ scaleX: 0, x: "+23vw" }}
            animate={{ scaleX: 1, x: 0 }}
            transition={{ duration: 1, ease: "easeOut", delay: 2 }}
          />
          <motion.div
            className="hero-line hero-line-2"
            initial={{ scaleX: 0, x: "-22vw" }}
            animate={{ scaleX: 1, x: 0 }}
            transition={{ duration: 1, ease: "easeOut", delay: 2 }}
          />
        </div>
        <div className="herox-main">
          <div>
            <motion.div
              className="cont"
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              transition={{ delay: 2.5 }}
            >
              <h1 className="herox-main-text">Hello There👋</h1>
              <motion.div
                initial={{ width: "100%" }}
                animate={{ width: 0 }}
                transition={{ duration: 1, ease: "easeOut", delay: 4.5 }}
                className="herox-main-text-mask"
              />
            </motion.div>
          </div>
          <motion.div
            className=" hero-line-3"
            initial={{ scaleY: 0 }}
            animate={{ scaleY: 1 }}
            transition={{ duration: 1, ease: "easeOut", delay: 3.5 }}
          />
          <div>
            <p>Click this button for main Action</p>
            <button>Click me</button>
          </div>
        </div>
      </div>
    </>
  );
}

export default Hero;
