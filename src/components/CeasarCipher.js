// src/components/NihilistCipher.js
import React, { useState } from 'react';
import './CipherStyles.css'; 

const CeasarCipher = () => {
  const [inputText, setInputText] = useState('');
  const [encodedText, setEncodedText] = useState('');

  const encodeCeasarCipher = () => {
    // Aquí puedes agregar la lógica de cifrado Bacon que desees
    setEncodedText(`Encoded version of: ${inputText}`);
  };  

  return (
    <div className="cipher-container">
      <h2 className="title">Ceasar Cipher</h2>
      <textarea
        className="cipher-textarea"
        value={inputText}
        onChange={(e) => setInputText(e.target.value)}
        placeholder="Enter text to encode"
        rows="5"
        cols="50"
      />

      <div className="cipher-button-container">
        <button className="cipher-button" onClick={encodeCeasarCipher}>Encode</button>
      </div >
      {encodedText && <p className='encoded-message'>Encoded Message: {encodedText}</p>}
    </div>
  );
};

export default CeasarCipher;
