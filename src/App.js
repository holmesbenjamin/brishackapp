import React, { useState, useEffect } from 'react';
import './App.css'; 
import Camera from './Camera';
import Blurb from './Blurb';
function App() {
  

  return (
    <div className="app-container">
      <h1 className="app-title">FruitCam</h1> 
      <Camera />
      <Blurb />
     
    </div>
  );
}

export default App;
