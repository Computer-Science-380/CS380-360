import React, { Component } from 'react';
import { Link } from 'react-router-dom'; // Importa Link desde react-router-dom
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
            <Link to="/">LOGO</Link> {/* Actualizamos el logo para redirigir a la página principal */}
          </div>

          {/* Navbar Links */}
          <ul id="menu">
            <li><Link to="/">Home</Link></li> {/* Enlace a la página principal */}
            <li><Link to="/services">Services</Link></li> {/* Modifica según tus rutas */}
            <li><Link to="/about">About</Link></li> {/* Enlace a la página About */}
            <li><Link to="/contact">Contact</Link></li> {/* Modifica según tus rutas */}
          </ul>
        </div>
      </nav>
    );
  }
}

export default Navbar;
