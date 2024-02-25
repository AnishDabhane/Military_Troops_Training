import React, { useState, useEffect, useRef } from "react";
import Lenis from "@studio-freight/lenis";
import "./PoseOverview.css";
import { useScroll, useTransform, motion } from "framer-motion";
import S1 from "/S1.webp";
import S2 from "/prone-shooting.jpg";
import SX from "/SX.jpg";
import S3 from "/Breve.jpg";
import S4 from "/sword.jpg";
import S5 from "/bamboo.webp";

function PoseOverview() {
  useEffect(() => {
    const lenis = new Lenis();
    function raf(time) {
      lenis.raf(time);
      requestAnimationFrame(raf);
    }
    requestAnimationFrame(raf);
  }, []);
  const container = useRef(null);
  const { scrollYProgress } = useScroll({
    target: container,
    offset: ["start start", "end end"],
  });
  const scale = useTransform(scrollYProgress, [0, 1], [1, 4]);
  const scale4 = useTransform(scrollYProgress, [0, 1], [1, 4]);
  const scale5 = useTransform(scrollYProgress, [0, 1], [1, 5]);
  const scale6 = useTransform(scrollYProgress, [0, 1], [1, 6]);
  const scale8 = useTransform(scrollYProgress, [0, 1], [1, 8]);
  const scale9 = useTransform(scrollYProgress, [0, 1], [1, 9]);
  const pictures = [
    {
      src: SX,
      scale: scale4,
    },
    {
      src: S1,
      scale: scale5,
    },
    {
      src: S3,
      scale: scale6,
    },
    {
      src: S2,
      scale: scale8,
    },
    {
      src: S4,
      scale: scale9,
    },
    {
      src: S5,
      scale: scale6,
    },
  ];
  return (
    <div ref={container} className="PO-container">
      <div className="PO-sticky">
        {pictures.map(({ src, scale }, index) => {
          return (
            <motion.div key={index} style={{ scale }} className="PO-el">
              <div className="PO-imageContainer">
                <img src={src} />
              </div>
            </motion.div>
          );
        })}
      </div>
    </div>
  );
}

export default PoseOverview;
