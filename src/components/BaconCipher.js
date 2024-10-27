// src/components/BaconCipher.js
import React, { useState } from 'react';
import './CipherStyles.css'; // Asegúrate de tener este archivo para los estilos

const BaconCipher = () => {
  const [inputText, setInputText] = useState('');
  const [encodedText, setEncodedText] = useState('');

  async function encryptMorse(text) {
    const response = await fetch('http://127.0.0.1:5000/api/morse', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ message: text }),
    });
    const data = await response.json();
    console.log(data.result);
    return data.result;
  }

  const encodeBaconCipher = async () => {
    //setEncodedText(`Encoded version of: ${inputText}`);
    const result = await encryptMorse(inputText);
    if (result) {
      setEncodedText(result);
    } else {
      setEncodedText('Error encoding message'); // Handle error case
    }

  };

  return (
    <div className="cipher-container">
      <h2 className="title">Bacon Cipher</h2>
      <textarea
        className="cipher-textarea"
        value={inputText}
        onChange={(e) => setInputText(e.target.value)}
        placeholder="Enter text to encode"
        rows="5"
        cols="50"
      />
      {/* Container to center the button */}
      <div className="cipher-button-container">
        <button className="cipher-button" onClick={encodeBaconCipher}>Encode</button>
      </div>
      {encodedText && <p className='encoded-message'>Encoded Message: {encodedText}</p>}
    </div>
  );
};

export default BaconCipher;