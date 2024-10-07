// src/components/Navbar.js
import React, { Component } from 'react';
import './Navbar.css'; // Import the CSS for styling

class Navbar extends Component {
  constructor(props) {
    super(props);
    this.state = {
      menuToggle: false,
    };
  }

  render() {
    return (
      <nav id="navbar" className="navbar">
        <div className="nav-wrapper">
          {/* Navbar Logo */}
          <div className="logo">
            {/* Replace "LOGO" with an image or custom text if desired */}
            <a href="#home">LOGO</a>
          </div>
          
          {/* Navbar Links */}
          <ul id="menu">
            <li><a href="#home">Home</a></li>
            <li><a href="#services">Services</a></li>
            <li><a href="#about">About</a></li>
            <li><a href="#contact">Contact</a></li>
          </ul>
        </div>
      </nav>
    );
  }
}

export default Navbar;
