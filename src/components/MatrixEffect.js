// src/components/MatrixEffect.js
import React, { useEffect } from 'react';
import './MatrixEffect.css';

const MatrixEffect = () => {
  useEffect(() => {
    const canvas = document.getElementById('matrix');
    const ctx = canvas.getContext('2d');

    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;

    const letters = Array.from({ length: 256 }, () => Math.random() * window.innerHeight);
    const fontSize = 16;

    const draw = () => {
      ctx.fillStyle = 'rgba(0, 0, 0, 0.05)'; // Fondo negro translúcido
      ctx.fillRect(0, 0, canvas.width, canvas.height);
      ctx.fillStyle = '#00ff00'; // Color verde neón de la "Matrix"
      ctx.font = `${fontSize}px monospace`;

      letters.forEach((yPos, index) => {
        const text = String.fromCharCode(65 + Math.random() * 33); // Genera caracteres aleatorios
        const xPos = index * fontSize;
        ctx.fillText(text, xPos, yPos);

        letters[index] = yPos > canvas.height + Math.random() * 1e4 ? 0 : yPos + fontSize;
      });
    };

    const interval = setInterval(draw, 70); // Ajusta la velocidad del efecto

    return () => clearInterval(interval); // Limpia el intervalo cuando el componente se desmonta
  }, []);

  return <canvas id="matrix"></canvas>;
};

export default MatrixEffect;
