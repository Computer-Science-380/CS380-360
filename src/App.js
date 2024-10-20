  // src/App.js
  import React from 'react';
  import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
  import Navbar from './components/Navbar';
  import MainMenu from './components/MainMenu';
  import MatrixEffect from './components/MatrixEffect'; // Importa el efecto Matrix
  import BaconCipher from './components/BaconCipher'; // Importa el componente BaconCipher
  import './App.css';
  import MorseCipher from './components/MorseCipher';
  import EncryptPage from './components/EncryptPage';
  import DecryptPage from './components/DecryptPage';

  function App() {
    return (
      <Router>
        <div className="App">
          <MatrixEffect /> {/* Inserta el efecto Matrix */}
          <Navbar />
          <Routes>
            <Route path="/" element={<MainMenu />} />
            <Route path="/encrypt" element={<EncryptPage />} /> {/* Ruta para BaconCipher */} 
            <Route path="/decrypt" element={<DecryptPage />} /> {/* Ruta para MorseCipher */}
            <Route path="/about" element={<div>About Page</div>} />
          </Routes>
        </div>
      </Router>
    );
  }

  export default App;
