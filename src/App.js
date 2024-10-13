  // src/App.js
  import React from 'react';
  import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
  import Navbar from './components/Navbar';
  import MainMenu from './components/MainMenu';
  import MatrixEffect from './components/MatrixEffect'; // Importa el efecto Matrix
  import BaconCipher from './components/BaconCipher'; // Importa el componente BaconCipher
  import MorseCipher from './components/MorseCipher'; // Importa el componente MorseCipher
  import './App.css';

  function App() {
    return (
      <Router>
        <div className="App">
          <MatrixEffect /> {/* Inserta el efecto Matrix */}
          <Navbar />
          <Routes>
            <Route path="/" element={<MainMenu />} />
            <Route path="/bacon" element={<BaconCipher />} /> {/* Ruta para BaconCipher */}
            <Route path="/morse" element={<MorseCipher />} /> {/* Ruta para MorseCipher */}
            <Route path="/about" element={<div>About Page</div>} />
          </Routes>
        </div>
      </Router>
    );
  }

  export default App;
