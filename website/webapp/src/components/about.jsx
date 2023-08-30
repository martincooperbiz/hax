import React from "react";
import INFO from "../data/user";
import CONFIG from "../data/config";

import "./styles/about.css";

const About = () => {
  return (
    <React.Fragment>
      <div className="about-content">
        <div id="about" className="about-container">
          <h1 className="title about-title">{INFO.about.title}</h1>
          <p className="main-text about-subtitle">{INFO.about.description}</p>
          <img src={CONFIG.IMAGES_URL + "HaX.png"} alt="logo"></img>
        </div>
      </div>
    </React.Fragment>
  );
};

export default About;
