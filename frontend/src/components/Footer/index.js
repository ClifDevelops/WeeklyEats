import React from "react";
import "./Footer.css";

const Footer = () => {
  return (
    <div className="footer-container">
      <div className="footer-info">
        <div className="footer-name">Robert Burroughs</div>
        <a href="https://github.com/ClifDevelops" className="footer-links">
          Github
        </a>
        <a
          href="https://www.linkedin.com/in/robert-burroughs-436300b7/"
          className="footer-links"
        >
          LinkedIn
        </a>
      </div>
    </div>
  );
};

export default Footer;
