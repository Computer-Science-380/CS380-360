  // src/App.js
  import React from 'react';
  import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
  import Navbar from './components/Navbar';
  import MainMenu from './components/MainMenu';
  import MatrixEffect from './components/MatrixEffect'; 
  import BaconCipher from './components/BaconCipher'; 
  import MorseCipher from './components/MorseCipher';
  import EncryptPage from './components/EncryptPage';
  import DecryptPage from './components/DecryptPage';
  import NihilistCipher from './components/NihilistCipher';
  import CeasarCipher from './components/CeasarCipher';
  import './App.css';


  function App() {
    return (
      <Router>
        <div className="App">
          <MatrixEffect /> 
          <Navbar />
          <Routes>
            <Route path="/" element={<MainMenu />} />
            <Route path="/encrypt" element={<EncryptPage />} />  
            <Route path="/decrypt" element={<DecryptPage />} /> 
            <Route path="/bacon" element={<BaconCipher/>} />
            <Route path="/morse" element={<MorseCipher/>} />
            <Route path="/ceasar" elemet={<CeasarCipher/>} />
            <Route path="/nihilist" element={<NihilistCipher/>} />


            <Route path="/about" element={<div>About Page</div>} />
          </Routes>
        </div>
      </Router>
    );
  }

  export default App;
