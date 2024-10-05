import React from 'react';
import './MainMenu.css'; // Creamos un archivo CSS separado para el estilo

const MainMenu = () => {
    return (
        <div className="main-menu">
            <h1>What would you like to do?</h1>
            <div className="menu-buttons">
                <button className="menu-button">Word Search</button>
                <button className="menu-button">Substitution Cipher</button>
                <button className="menu-button">Unscrambler</button>
                <button className="menu-button highlight">Encrypt a Message</button>
            </div>
        </div>
    );
};

export default MainMenu;