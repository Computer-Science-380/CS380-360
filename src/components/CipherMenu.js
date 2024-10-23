import { useNavigate } from 'react-router-dom'; // Importa useNavigate
import React, { useEffect } from 'react';
import './CipherMenu.css';

const CipherMenu = () => {
  const navigate = useNavigate(); // Inicializa useNavigate aquí

  // Función para agregar y eliminar la clase glitch
  useEffect(() => {
    const buttons = document.querySelectorAll('.cipher-menu-button span'); // Selecciona todos los spans de los botones

    const applyGlitch = () => {
      buttons.forEach((button) => {
        button.classList.add('glitch-active'); 
      });

      // Después de un tiempo (300ms), eliminamos la clase de glitch
      setTimeout(() => {
        buttons.forEach((button) => {
          button.classList.remove('glitch-active');
        });
      }, 300); // Duración del glitch
    };

    // Función que ejecuta el glitch de manera aleatoria entre 0 y 4 segundos
    const randomIntervalGlitch = () => {
      applyGlitch();
      const randomTime = Math.random() * 4000;
      setTimeout(randomIntervalGlitch, randomTime); 
    };

    randomIntervalGlitch();
  }, []);

  return (
    <div className="main-menu">
      <h1 className="title">What would you like to do?</h1>
      <div className="cipher-menu-buttons">
        <button className="cipher-menu-button" > 
          <span>BACON</span>
        </button>
        <button className="cipher-menu-button" >
          <span>MORSE</span>
        </button>
        <button className="cipher-menu-button" >
          <span>CEASAR</span>
        </button>
        <button className="cipher-menu-button" >
          <span>NIHILIST</span>
        </button>
      </div>
    </div>
  );
};

export default CipherMenu;
