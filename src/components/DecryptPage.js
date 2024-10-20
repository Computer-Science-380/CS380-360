import { useNavigate } from 'react-router-dom';
import React, { useEffect } from 'react';
import './CipherMenu.css'; // Asegúrate de tener CipherMenu.css importado correctamente

const CipherMenu = () => {
  const navigate = useNavigate();

  useEffect(() => {
    const buttons = document.querySelectorAll('.cipher-menu-button span');

    const applyGlitch = () => {
      buttons.forEach((button) => {
        button.classList.add('glitch-active');
      });

      setTimeout(() => {
        buttons.forEach((button) => {
          button.classList.remove('glitch-active');
        });
      }, 300);
    };

    const randomIntervalGlitch = () => {
      applyGlitch();
      const randomTime = Math.random() * 4000;
      setTimeout(randomIntervalGlitch, randomTime);
    };

    randomIntervalGlitch();
  }, []);

  return (
    <div className="main-menu">
      <h1 className="title">Select a Cipher</h1>
      <div className="cipher-menu-buttons">  {/* Usamos el mismo contenedor para los botones */}
        <button className="cipher-menu-button" onClick={() => navigate('/bacon')}>
          <span>BACON</span>
        </button>
        <button className="cipher-menu-button" onClick={() => navigate('/morse')}>
          <span>MORSE</span>
        </button>
        <button className="cipher-menu-button" onClick={() => navigate('/caesar')}>
          <span>CEASAR</span>
        </button>
        <button className="cipher-menu-button" onClick={() => navigate('/nihilist')}>
          <span>NIHILIST</span>
        </button>
      </div>
    </div>
  );
};

export default CipherMenu;
