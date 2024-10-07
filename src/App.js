// src/App.js
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Navbar from './components/Navbar';
import MainMenu from './components/MainMenu';
import './App.css';

function App() {
  return (
    <Router>
      <div className="App">
        <Navbar />
        <Routes>
          <Route path="/" element={<MainMenu />} />
          <Route path="/about" element={<div>About Page</div>} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
