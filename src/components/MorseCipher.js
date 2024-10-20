<<<<<<< Updated upstream
    // src/components/BaconCipher.js
    import React, { useState } from 'react';
    import './CipherStyles.css'; // Asegúrate de tener este archivo para los estilos

    const MorseCipher = () => {
    const [inputText, setInputText] = useState('');
    const [encodedText, setEncodedText] = useState('');

    const encodeMorseCipher = () => {
        // Aquí puedes agregar la lógica de cifrado Bacon que desees
        setEncodedText(`Encoded version of: ${inputText}`);
    };  

    return (
        <div className="cipher-container">
        <h2 className="title"> Morse Cipher</h2>
        <textarea
            className="cipher-textarea"
            value={inputText}
            onChange={(e) => setInputText(e.target.value)}
            placeholder="Enter text to encode"
            rows="5"
            cols="50"
        />
        {/* Contenedor para centrar el botón */}
        <div className="cipher-button-container">
            <button className="cipher-button" onClick={encodeMorseCipher}>Encode</button>
        </div >
        {encodedText && <p className='encoded-message'>Encoded Message: {encodedText}</p>}
        </div>
    );
    };

    export default MorseCipher;
=======
// src/components/BaconCipher.js
import React, { useState } from 'react';
import './CipherStyles.css'; // Asegúrate de tener este archivo para los estilos

const MorseCipher = () => {
  const [inputText, setInputText] = useState('');
  const [encodedText, setEncodedText] = useState('');

  const encodeMorseCipher = () => {
    // Aquí puedes agregar la lógica de cifrado Bacon que desees
    setEncodedText(`Encoded version of: ${inputText}`);
  };

  return (
    <div className="cipher-container">
      <h2 className="title">Morse Cipher</h2>
      <textarea
        className="cipher-textarea"
        value={inputText}
        onChange={(e) => setInputText(e.target.value)}
        placeholder="Enter text to encode"
        rows="5"
        cols="50"
      />
      {/* Contenedor para centrar el botón */}
      <div className="cipher-button-container">
        <button className="cipher-button" onClick={encodeBaconCipher}>Encode</button>
      </div >
      {encodedText && <p className='encoded-message'>Encoded Message: {encodedText}</p>}
    </div>
  );
};

export default BaconCipher;
>>>>>>> Stashed changes
