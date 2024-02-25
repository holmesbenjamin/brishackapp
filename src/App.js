import React, { useState, useEffect } from 'react';
import './App.css'; 
import Camera from './Camera';
import Blurb from './Blurb';
import Logo from './Logo';
import Button from './Button';


function App() {
  

  return ( 
    <>

    <div className="app-container">
    <Logo/>
      {/* <h1 className="app-title">FruitCam</h1>  */}
      <Camera />

      <Blurb />
     
    </div>
    </>
  );
}

export default App;
